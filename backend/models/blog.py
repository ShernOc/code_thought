#create , update blog delete a blog 
import sqlalchemy

from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime 

from sqlalchemy.orm import declarative_base, relationship 

Base = declarative_base()

class Blog(Base):
    
    __tablename__ = 'blogs'
    
    id = Column(Integer,primary_key = True)
    
    title = Column(String, nullable =False)
    
    content = Column(String, nullable=False)
    
    author_id = Column(Integer, ForeignKey('user.id'))
    
    #relationship
    author = relationship('User', back_populates='blogs')
    
    comments = relationship('Comment',back_populates='blogs')
    
    
    
    
    
    
    