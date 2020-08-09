#!/usr/bin/python3
""" add the state object “Louisiana” """

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new = State(name='Louisiana')
    session.add(new)
    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    session.commit()
    print("{}".format(new_state.id))
    session.close()
