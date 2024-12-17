from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime 

from sqlalchemy.orm import declarative_base, relationship,backref

Base = declarative_base()

class Admin: 
    __tablename__ = 'admins'
    
    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = True)
    email = Column(String, nullable= True)
    
    #relations 
       # Relationship with users, posts, and comments
    users = relationship('User', backref='admin', lazy='dynamic')
    blogs = relationship('Post', backref='admin', lazy='dynamic')
    comments = relationship('Comment', backref='admin', lazy='dynamic')
    
    # def __init__(self,user_name,email ):
    #     self.user_name = user_name
    #     self.email = email
        
        
        
    