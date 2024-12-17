#create comment , update, delete, 
from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime 

from sqlalchemy.orm import declarative_base, relationship 

Base = declarative_base()

class Comment(Base): 
    __tablename__ = 'comments'
    
    id = Column(Integer,primary_key = True)
    
    content = Column(String, nullable=False)
    
    blog_id = Column(Integer,ForeignKey('blog.id'), nullable=False)
    author_id = Column(Integer,ForeignKey('users.id'))
    
    #relationship
    blog = relationship('Blog', back_populates = 'comments')
    
    author = relationship('User', back_populates='comments')
    
    
    
    
    # def __init__(self,name,mail):
    #     self.name = name 
    #     self.email = email 
        
    # @property
    # def name(self):
    #     return self._name 
    
    # @name.setter
    # def name(self,value):
    #     if isinstance(value,str):
    #         self._name = value 
    #     else: 
    #         ValueError("The name has to be provided")  
    
    # @property
    # def email(self):
    #     return self._email
    
    # @email.setter
    # def email(self,value):
    #     pattern = '[a-zA-Z0-9]+@[a-zA-Z]+(\.com|\.edu|\.net)'
    #     while True:
    #         if re.match(pattern,value):
    #             return re.search(pattern,value)
    #             break
    #         else: 
    #             ValueError("The email has to be of a certain numbers. ")
                
    
                