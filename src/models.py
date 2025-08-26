from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.orm import (
    declared_attr
)

import config
from db import BaseModelType


__all__ = ('Employee', )


class BaseColumnsMixin:
    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True, autoincrement=True)
    
    @declared_attr
    def created_at(cls):
        return Column(DateTime, nullable=False, default=cls.get_now)
    
    @declared_attr
    def updated_at(cls):
        return Column(DateTime, nullable=False, default=cls.get_now, onupdate=cls.get_now)
    
    @classmethod
    def get_now(cls):
        return datetime.now(ZoneInfo(config.TIME_ZONE))


class Employee(BaseModelType, BaseColumnsMixin):
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Slut(BaseModelType, BaseColumnsMixin):
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
