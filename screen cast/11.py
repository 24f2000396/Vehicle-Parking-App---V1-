import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column,Integer,String, ForeignKey
from sqlalchemy import select


from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'user' 
    user_id = Column(Integer , autoincrement=True,primary_key=True)
    user_email = Column(String(50), unique =True, nullable=True)
    