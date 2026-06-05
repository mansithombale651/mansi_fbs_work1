#WAP to check if user has intered correct user iid or password

user_id=3651
u_password="admin"

#take input
userid=int(input(" Enter user id:"))
password=str(input("Enter password:"))

if(userid == user_id  and  password == u_password):
    print("login succwssful")

else:
    print("Invalid user id or password")
