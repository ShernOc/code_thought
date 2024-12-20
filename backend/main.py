# here you import 
#importing uvicorn
import uvicorn 
from config import get_db
from authentication import get_current_user,get_password_hash
from models import *
from sqlalchemy.orm import Session
from fastapi import FastAPI,HTTPException, Depends, status
from typing import List
from app.api import hashed_password
from app.api import app



if __name__ == "__main__":
    uvicorn.run("app.api:app", 
                host = "127.0.0.1",
                port = 8000, 
                reload=True)
    

# create the CRUD functions here and test them. 
@app.post("/login")
def register_user(user_name: str, password: str, email: str, db:Session = Depends(get_db)):
    password = get_password_hash(password)
    user = User(username=user_name, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "User created successfully"}


@app.get("/blogs", response_model=List[dict])
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return [{"id": blog.id, "title": blog.title, "content": blog.content, "user": blog.user.user_name} for blog in blogs]

@app.post("/blogs")
def create_blog(title: str, content: str, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    blog = Blog(title=title, content=content, user_id=user.id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

@app.post("/comments")
def add_comment(blog_id: int, content: str, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    comment = Comment(content=content, blog_id=blog_id, user_id=user.id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

@app.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    db.delete(comment)
    db.commit()
    return {"msg": "Comment deleted successfully"}