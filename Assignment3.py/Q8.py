# WAP to prompt user to enter userid and password. 
# After verifying user id amd password display a 4 digit random number and ask user to enter the same.
# if user enters the same number then shoe him successful message otherwise failed (like captcha)

import random

user_id=3651
u_password="admin1"

#take input
userid=int(input('Enter User id:'))
password=str(input('Enter password:'))

if (userid ==user_id and password == u_password ):
    print('Login successful.')

    #Generate 4 digit random number
    captcha=random.randint(1000,9999)
    print("Enter the number:",captcha)

    u_input= int(input("Reenter the number:"))

     #check captcha
     
    if(u_input == captcha):
        
          print("Verification successful.")
    else:
        print("Verification failed.")


else:
 print("invalid user id or password")
     