# here you import 
from config import * 

# create the CRUD functions here and test them. 
def create_user(user_name):
    user= User(user_name = user_name)
    #add to a session 
    session.add(user)
    session.commit()
    return user

#The create a blog
def create_blog(title,content,user_id):
    blog = Blog(title = title, content = content, user_id = user_id)
    
    session.add(blog)
    session.commit()
    return blog

def create_comment(content,blog_id,user_id):
    comment = Comment(content= content,blog_id = blog_id, user_id = user_id)
    session.add(comment)
    session.commit()
    return comment




    
    


    
    
    








#test the work. 
user1 = create_user("Sherlyne")
print("Created user", user1.user_name)

blog1 = create_blog("Life", "Life is beautiful so are you", 1)
print(blog1.user_id,"created", blog1)

comment1 = create_comment("Great concept",1,1)
print(comment1.user_id, "has written this", comment1.content)

