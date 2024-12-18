from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

# from models import admin, blog, comment,user
from models import User,Blog,Comment,Admin

from models import Base, User, Blog, Comment, Admin  # Import your models

#seed.py is a file you for generation/populates random data. 

# The process of adding sample data to the database as "seeding." the database. 


