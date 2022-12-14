import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    follower = relationship("Follower", uselist=False, backref="user")
    comment = relationship("Comment", uselist=False, backref='user')
    post = relationship("Post", uselist=False, backref='user')

    def sign():
        return {}
    def updateProfile():
        return {}
    def likePost():
        return {}
    def comment():
        return {}
    def logOut():
        return {}
    def savePost():
        return {}
    def followerUser():
        return {}
    def disfollowerUser():
        return {}
    def createPost():
        return {}
    def deletePost():
        return {}
    

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True) 
    comment_text = Column(String, nullable=False)

    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True) 
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment = relationship("Comment", uselist=False, backref='post')
    media = relationship("Media", uselist=False, backref='post')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True) 
    type_ = Column(String, nullable=False)
    url = Column(String, nullable=False)

    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)




# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e