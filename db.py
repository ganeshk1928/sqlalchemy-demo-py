from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine("mysql://<Username>:<Password>@<Host>:<Port>/<Database name>")
engine = create_engine("mysql://root:@localhost:3306/sqlalch")
connection = engine.connect()

Session = sessionmaker(bind=engine)
Base = declarative_base()
metadata = MetaData()


class Details(Base):
    __tablename__ = 'details'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)

Base.metadata.create_all(engine)

def insert_row(name, email):
    session = Session()
    add_details = Details(name = name, email = email)
    session.add(add_details)
    session.commit()


def get_details_by_id(id):
    session = Session()
    res = session.query(Details).filter(Details.id == id).first()
    session.close()
    return res


def get_all_details():
    session = Session()
    res = session.query(Details).all()
    session.close()
    return res


def update_name(id, name):
    session = Session()
    res = session.query(Details).filter(Details.id == id).update({'name': name})
    session.commit()
    session.close()
    return res


def delete_row(id):
    session = Session()
    res = session.query(Details).filter(Details.id == id).delete()
    session.commit()
    session.close()
    return res