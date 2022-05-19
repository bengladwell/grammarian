import pytest
from time import sleep
from sqlalchemy.sql.schema import Column
from sqlalchemy import create_engine
from sqlalchemy import Text
from sqlalchemy.orm import sessionmaker

from app.models.base import Base

class BasicModel(Base):
    __tablename__ = 'test_table'

    text = Column(Text, nullable=False)


engine = create_engine('sqlite:///data/test.db', echo=True)
Session = sessionmaker(bind=engine, autocommit=True)
session = Session()
Base.set_session(session)
BasicModel.metadata.create_all(engine)


@pytest.fixture
def test_obj():
    obj = BasicModel.find_or_create(text='this is a test')
    yield obj
    obj.delete()

class TestBase:
    def test_mixin_create(self):
        created_obj = BasicModel.create(text='this is a test')
        found_obj = BasicModel.query.filter_by(text='this is a test').first()
        assert created_obj.id == found_obj.id
        created_obj.delete()

    def test_find_or_create_find(self, test_obj):
        assert test_obj == BasicModel.find_or_create(text='this is a test')

    def test_find_or_create_create(self, test_obj):
        assert test_obj != BasicModel.find_or_create(text='a new obj')

    def test_created_at(self, test_obj):
        assert test_obj.created_at

    def test_updated_at(self, test_obj):
        test_obj
        sleep(1)
        test_obj.update(text="something different")
        assert test_obj.created_at != test_obj.updated_at
