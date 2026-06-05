# write a program to check if person is eligible for marriage or not(male age >=21 and female age >=18)

#input gender and age
gender=str(input('Enter gender(male/female):'))
age= int(input('Enter age :'))

#check eligibility
if(gender == "male" and age  >=21 ):
    print("eligible for marriage.")

elif(gender == "female" and age >=18):
    print("Eligible for marriage.")

else:
    print("Not eligible for marriage.")