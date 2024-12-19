from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime, UniqueConstraint, DateTime

from database.config import relationship, association_proxy,declarative_base


Base = declarative_base()

#Admin class  
class Admin(Base): 
    __tablename__ = 'admin'
    __table_arg__ = (UniqueConstraint('email',
            name='unique_email'),)
    
    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = False)
    email = Column(String, nullable= False)
    
    


