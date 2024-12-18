from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

# from models import admin, blog, comment,user
from models import User,Blog,Comment,Admin

engine = create_engine("sqlite:///code_thought.sqlite")


Session = sessionmaker(bind = engine)
session = Session()


