from sqlalchemy import String
from sqlalchemy.sql.schema import Column
from .base import Base


class Pos(Base):
    __tablename__ = 'pos'

    label = Column(String(5), nullable=False)
