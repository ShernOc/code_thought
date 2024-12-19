from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime, UniqueConstraint, DateTime

from database.config import relationship, association_proxy,declarative_base



Base = declarative_base()


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

