from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()
DB_CONNECT = 'mysql+pymysql://root:root@192.168.18.30:3306/logdata'
engine = create_engine(DB_CONNECT, echo=True)
DB_session = sessionmaker(bind=engine)
session = DB_session()


class Nonn(BaseModel):
    __tablename__ = 'nonns'
    id = Column(Integer(), primary_key=True)
    word = Column(String(1024))
    point = Column(String(50))

class Other(BaseModel):
    __tablename__ = 'others'
    id = Column(Integer(), primary_key=True)
    word = Column(String(1024))
    point = Column(String(50))


def init_db():
    BaseModel.metadata.create_all(engine)


def drop_db():
    BaseModel.metadata.drop_all(engine)

# drop_db()
# init_db()

