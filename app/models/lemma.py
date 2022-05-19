from sqlalchemy import String
from sqlalchemy.sql.schema import Column
from .base import Base


class Lemma(Base):
    __tablename__ = 'lemmas'

    text = Column(String(48), nullable=False)
