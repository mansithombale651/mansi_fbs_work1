#WAP to check if given 3 digit number is a palindrom or not

#take input
num=int(input("Enter the number:"))
temp=num

d1=temp%10
temp=temp//10

d2=temp%10
temp=temp//10

d3=temp%10
temp=temp//10

#check pallindron

if(d1 == d3):
    print('The number is pallindrom.')

else:
    print("The number is not a pallindrom")