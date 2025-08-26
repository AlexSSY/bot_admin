import inflect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeMeta

import config


inflector = inflect.engine()
engine = create_engine(f'sqlite:///{config.DB_NAME}')
SessionMaker = sessionmaker(engine, autoflush=False, autocommit=False)


class BaseModelTypeMeta(DeclarativeMeta):
    def __new__(cls, name, bases, namespace, **kwargs):
        if '__tablename__' not in namespace:
            namespace.update({
                '__tablename__': inflector.plural(name.lower())
            })
        return super().__new__(cls, name, bases, namespace, **kwargs)


BaseModelType = declarative_base(metaclass=BaseModelTypeMeta)
