from db import SessionMaker


def create_record(sa_model_class, **columns):
    with SessionMaker() as session:
        session.add(sa_model_class(**columns))
        session.commit()


def count(sa_model_class):
    with SessionMaker() as session:
        return session.query(sa_model_class).count()


def rows(sa_model_class, limit, offset):
    with SessionMaker() as session:
        return session.query(sa_model_class).limit(limit).offset(offset).all()


def detail(sa_model_class, id):
    with SessionMaker() as session:
        return session.query(sa_model_class).get(id)
