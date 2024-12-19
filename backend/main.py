# here you import 
#importing uvicorn
import uvicorn 
if __name__ == "__main__":
    uvicorn.run("app.api:app", 
                host = "127.0.0.1",
                port = 8000, 
                reload=True)
    


from config import session
from models import *

# create the CRUD functions here and test them. 
def create_user(user_name):
    user= User(user_name = user_name)
    #add to a session 
    session.add(user)
    session.commit()
    return user

#fetching user 
def fetch_user(user_id):
    return session.query(User).get(user_id)

#The create a blog
def create_blog(title,content,user_id):
    blog = Blog(title = title, content = content, user_id = user_id)
    
    session.add(blog)
    session.commit()
    return blog

def fetch_blog(blog_id):
    return session.query(Blog).get(blog_id)



def create_comment(content,blog_id,user_id):
    comment = Comment(content= content,blog_id = blog_id, user_id = user_id)
    session.add(comment)
    session.commit()
    return comment

def fetch_comment(blog_id):
    return session.query(Blog).get(blog_id)




