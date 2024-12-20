from faker import Faker
from config import session
from models import Blog,Comment,User


fake= Faker()
# generate random data of five database. 

#random users 
for _ in range(5):
    user = User(
        user_name = fake.name(), 
        email = fake.email(), 
        password =fake.password())

session.add(user)
session.commit()

#random blogs
users = session.query(User).all()
for _ in range(5):
    blog = Blog(
        title = fake.sentence(), 
        content = fake.text(),  user_id=fake.random_choices([user.id for user in users]) # random assignment of users. 
        )

session.add(blog)
session.commit()

#random comments
blogs = session.query(Blog).all() 
for _ in range(5):
    comment = Comment(
        content = fake.text(), 
        blog_id = fake.random_element([blog.id for blog in blogs]), user_id =fake.random_element([user.id for user in users]))

session.add(comment)
session.commit()

print("Random data will be displayed")
