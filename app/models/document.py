from sqlalchemy import String
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship
from .base import Base


class Document(Base):
    __tablename__ = 'documents'

    name = Column(String, nullable=False)
    sentences = relationship("Sentence")
