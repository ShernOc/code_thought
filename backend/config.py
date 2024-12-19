from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from sqlalchemy.ext.associationproxy import association_proxy

from models import User,Blog,Comment,Admin


engine = create_engine("sqlite:///code_thought.sqlite")

#import session maker 
Session = sessionmaker(bind = engine)
session = Session()


