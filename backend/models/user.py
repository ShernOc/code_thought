from sqlalchemy import create_engine

from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime 

from sqlalchemy.orm import declarative_base, relationship 

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = True)
    email = Column(String, nullable= True)
    password_hash = Column(String(128), nullable=False)
    
    #relationship 
    blogs= relationship('Blog',back_populates='author')
    
    comments = relationship('Comment',back_populates='author')

    # def __init__(self, id, user_name, ):
    #     self.id = id
    #     self.user_name = user_name
        
    # @property
    # def user_name(self):
    #     return self.user_name
    
    # @user_name.setter 
    # def user_name(self,value):
    #     if isinstance(value,str):
    #         if 0<len(value)>10:
    #             self._user_name =value
    #         else:
    #             TypeError("The value has to work")
                
            
            
        
        
        
        

        