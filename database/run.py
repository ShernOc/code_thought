import models

#test the work. 
user1 = create_user("Sherlyne")
print("Created user", user1.user_name)

blog1 = create_blog("Life", "Life is beautiful so are you", 1)
print(blog1.user_id,"created", blog1)

comment1 = create_comment("Great concept",1,1)
print(comment1.user_id, "has written this", comment1.content)

#fetch user by id run the function. 
# fetch_user = fetch_user(1)
# print(fetch_user.name)





