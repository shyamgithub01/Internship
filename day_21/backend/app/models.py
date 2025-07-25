from .database import Base
from sqlalchemy import Column , Integer , Boolean , String
from sqlalchemy import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer , primary_key=True , nullable=False)
    title = Column(String , nullable=False)
    content = Column(String , nullable=False)
    published = Column(Boolean , server_default='TRUE' , nullable=False)
    created_at = Column(TIMESTAMP(timezone=True) , nullable=False , server_default=text('now()'))

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer , nullable=False , primary_key=True)
    email = Column(String , nullable=False , unique= True)
    password = Column(String , nullable= False)
 