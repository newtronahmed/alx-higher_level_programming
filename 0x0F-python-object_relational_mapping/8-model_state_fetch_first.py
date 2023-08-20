#!/usr/bin/python3
"""prints the first State object from the database"""

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

    row = session.query(State).order_by(State.id).first()
    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")
