#WAP to reverse three-digit number


#take input
num=intd1=int(input("Enter the 3 digit number:"))

d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10


#perform operation
rev=d1*100+d2*10+d3*1
rev==num

#Display output
print("Reverce number is :",rev)


