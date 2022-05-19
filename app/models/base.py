"""
Exports Base - a sqlalchemy model to be inherited by other models
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer
from sqlalchemy.sql.schema import Column
from sqlalchemy_mixins import AllFeaturesMixin, TimestampsMixin

DeclarativeBase = declarative_base()

class Base(DeclarativeBase, AllFeaturesMixin, TimestampsMixin):
    __abstract__ = True

    id = Column(Integer, primary_key=True)

    @classmethod
    def find_or_create(cls, **kwargs):
        """If matching entity exists, return it.
        If not, create it and return it."""

        found = cls.query.filter_by(**kwargs).first()

        if found:
            return found

        return cls.create(**kwargs)
