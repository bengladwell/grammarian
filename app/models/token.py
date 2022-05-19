from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.sql.schema import Column
from .base import Base


class Token(Base):
    __tablename__ = 'tokens'

    sentence_id = Column(Integer, ForeignKey('sentences.id'), nullable=False)
    sentence_index = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    lemma_id = Column(Integer, ForeignKey('lemmas.id'), nullable=False)
    pos_id = Column(Integer, ForeignKey('pos.id'), nullable=False)
    morph = Column(String(255))
