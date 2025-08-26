import sys

from IPython import embed
from faker import Faker

from models import Employee, Slut
from db import BaseModelType, engine, SessionMaker


def create_all():
    BaseModelType.metadata.create_all(engine)
    print("All tables created")


def drop_all():
    BaseModelType.metadata.drop_all(engine)
    print("All tables dropped")


def reset():
    drop_all()
    create_all()


def seed():
    fake = Faker()
    with SessionMaker() as session:
        for _ in range(20):
            session.add(Employee(first_name=fake.first_name(), last_name=fake.last_name()))
            session.add(Slut(first_name=fake.first_name(), last_name=fake.last_name()))
        session.commit()



def main():
    if len(sys.argv) > 1:
        func_name = sys.argv[1]
        if func_name in globals() and callable(globals()[func_name]):
            globals()[func_name]()
        else:
            print(f"Function '{func_name}' not found")
    else:
        banner = "Welcome to DB Manager shell. Try: create_all(), drop_all()"
        embed(header=banner, user_ns=globals())


if __name__ == "__main__":
    main()
