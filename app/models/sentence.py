from sqlalchemy import Integer, Text, ForeignKey
from sqlalchemy.sql.schema import Column
from .base import Base


class Sentence(Base):
    __tablename__ = 'sentences'

    text = Column(Text, nullable=False)
    document_id = Column(Integer, ForeignKey('documents.id'), nullable=False)
    document_index = Column(Integer, nullable=False)
