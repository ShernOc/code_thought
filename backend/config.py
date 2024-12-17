from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from models.admin import Admin
from models.blog import  Blog
from models.comment import Comment
from models.user import User

engine = create_engine("sqlite:///code_thought.sqlite")


Session = sessionmaker(bind = engine)
session = Session()


