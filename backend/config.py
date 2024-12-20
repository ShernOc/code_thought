from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,  declarative_base, relationship


from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine("sqlite:///code_thought.sqlite")

#import session maker 
Session = sessionmaker(bind = engine)
session = Session()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

