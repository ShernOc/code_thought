from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime, UniqueConstraint, DateTime

from database.config import relationship, association_proxy,declarative_base

from comment import Comment # Comment class

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __table_arg__ = (UniqueConstraint ('email',
                    name='unique_email'),)
    
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = True)
    email = Column(String, nullable= True)
    password = Column(String(128), nullable=False)
    # created_at = Column(DateTime, default_default= datetime.utcnow())
    # updated_at = Column(DateTime, onupdate=datetime.utcnow())
    
    #relationship with blog
    blogs= association_proxy('comments', 'blog',creator = lambda bl:Comment(blog = bl))
    
    comments = relationship('Comment',back_populates='users')
