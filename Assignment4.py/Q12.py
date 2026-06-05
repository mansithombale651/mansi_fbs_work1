#Write a program to check if given number is Armstrong number or not. 

#input number
num=int(input("Enter a number:"))

temp=num
count=0
sum=0

#count number of digit
t=num
while (t>0):
    count=count+1
    t//=10

#calculate armstrong sum
while(temp>0):
    digit=temp%10
    sum=sum+(digit**count)
    temp//=10

#check condition
if(sum==num):
    print("Armstrong number.")

else:
    print("Not a armstrong number")
