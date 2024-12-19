from faker import Faker

from config import * 

from models import Admin, Blog,Comment,User

fake= Faker()
# generate random data of five database. 

#random users 
for _ in range(5):
    user = User(user_name = fake.user_name(), email = fake.email(), password =fake.password())

session.add(user)
session.commit()

#random blogs
for _ in range(5):
    blog = Blog(title = fake.title(), content = fake.content(),  user_id=fake.user_id())

session.add(blog)
session.commit()

#random comments
for _ in range(5):
    comment = Comment(content = fake.content(), blog_id = fake.blog_id(), user_id =fake.user_id())

session.add(comment)
session.commit()

#random admin
for _ in range(2):
    admin = Admin(user_name = fake.user_name(), content = fake.content(),  user_id=fake.user_id())

session.add(admin)
session.commit()

#   Accessing the uses, blogs,comments
admin1 = session.query(Admin).first()









