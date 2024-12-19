from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy.orm import declarative_base, relationship 


# from models import admin, blog, comment,user
from models.user import User
from models.admin import Admin
from models.blog import Blog
from models.comment import Comment

engine = create_engine("sqlite:///code_thought.sqlite")

#import session maker 
Session = sessionmaker(bind = engine)
session = Session()


