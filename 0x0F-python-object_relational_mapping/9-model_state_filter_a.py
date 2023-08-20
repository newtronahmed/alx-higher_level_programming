#!/usr/bin/python3
"""lists all State objects that contain the letter a """

if __name__ == "__main__":

    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).filter(State.name.like("%a%"))\
                  .order_by(State.id).all()
    for row in rows:
        print("{}: {}".format(row.id, row.name))
