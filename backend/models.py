
from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime, UniqueConstraint, DateTime

from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy.orm import declarative_base,  association_proxy, relationship, backref, association_proxy

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __table_arg__ = (UniqueConstraint ('email',
                    name='unique_email'),)
    
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = True)
    email = Column(String, nullable= True)
    password = Column(String(128), nullable=False)
    created_at = Column(DateTime, default_default= datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())
    
    #relationship with blog
    blogs= association_proxy('comments', 'blog',creator = lambda gm:Comment(blog = gm))
    
    comments = relationship('Comment',back_populates='users')


    #blog content class 
class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer,primary_key = True)
    title = Column(String, nullable =False)
    content = Column(String, nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))
    
    #relationship
    user= relationship('User', back_populates='blogs')
    
    comments = relationship('Comment',back_populates='blogs')
    
    #Comment class: 
class Comment(Base): 
    __tablename__ = 'comments'
    
    id = Column(Integer,primary_key = True)
    
    content = Column(String, nullable=False)
    
    user_id = Column(Integer,ForeignKey('users.id'))
    blog_id = Column(Integer,ForeignKey('blogs.id'), nullable=False)
    
    #relationship
    user= relationship('User', back_populates='comments') 
    
    blog = relationship('Blog', back_populates = 'comments')
    
    
#Admin class  
class Admin(Base): 
    __tablename__ = 'admin'
    __table_arg__ = (UniqueConstraint('email',
            name='unique_email'),)
    
    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = False)
    email = Column(String, nullable= False)
    
    
  
    
    
    
    
    
    
    
    
    

                
            
            
        
        
        
        

        