from .database import Base 
from sqlalchemy import Boolean, Column, ForeignKey,Integer,String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
class Post(Base):
    __tablename__ = "post"
    id = Column(Integer,primary_key = True , nullable = False)
    title = Column(String,nullable = False )
    content = Column(String , nullable=False)
    published = Column(Boolean , nullable=False , server_default = 'TRUE') 
    created_at = Column(TIMESTAMP(timezone=True),nullable = False , server_default =text("now()"))
    owner_id = Column(Integer , ForeignKey("users.id" , ondelete="CASCADE") , nullable = False)
    owner = relationship("User")#get class


#new sqlalchemy model 
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True  ,nullable = False )
    email = Column(String,nullable = False ,unique=True)
    password = Column(String , nullable = False)
    created_at = Column(TIMESTAMP(timezone=True),nullable = False , server_default =text("now()"))


class Votes(Base):
    __tablename__ = "votes"
    user_id = Column(Integer , ForeignKey("users.id" , ondelete="CASCADE") , primary_key = True)
    post_id = Column(Integer , ForeignKey("post.id" , ondelete="CASCADE") , primary_key = True)
    



