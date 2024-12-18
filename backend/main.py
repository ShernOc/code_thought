# here you import 
from config import * 

# create the CRUD functions here and test them. 
def create_user(user_name):
    user= User(user_name = user_name)
    #add to a session 
    session.add(user)
    session.commit()
    return user


    
    
    








#test the work. 
user1 = create_user("Sherlyne")
print("Created user", user1.user_name)