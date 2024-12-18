
from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime, UniqueConstraint

from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __table_arg__ = (UniqueConstraint ('email',
                    name='unique_email'),)
    
    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = True)
    email = Column(String, nullable= True)
    password = Column(String(128), nullable=False)
    # blog_id = Column(Integer, ForeignKey ("blogs.id"))
    
    #relationship 
    blogs= relationship('Blog',back_populates='users')
    
    comments = relationship('Comment',back_populates='users')
    
    #blog content class 
class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer,primary_key = True)
    title = Column(String, nullable =False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    #relationship
    user= relationship('User', back_populates='blogs')
    
    comments = relationship('Comment',back_populates='blogs')
    
    #Comment class: 
class Comment(Base): 
    __tablename__ = 'comments'
    
    id = Column(Integer,primary_key = True)
    
    content = Column(String, nullable=False)
    
    blog_id = Column(Integer,ForeignKey('blogs.id'), nullable=False)
    user_id = Column(Integer,ForeignKey('users.id'))
    
    #relationship
    blog = relationship('Blog', back_populates = 'comments')
    
    user= relationship('User', back_populates='comments')
    
    #Admin class 
    
class Admin(Base): 
    __tablename__ = 'admin'
    __table_arg__ = (UniqueConstraint('email',
            name='unique_email'),)
    
    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = False)
    email = Column(String, nullable= False)
    
    #Relationship with users, blog and comments tables 
    
    users = relationship('User', backref='admins')
    blogs = relationship('Blog', backref='admins')
    comments = relationship('Comment', backref='admins')
    
    
    
    
    
    
    
    
    

                
            
            
        
        
        
        

        