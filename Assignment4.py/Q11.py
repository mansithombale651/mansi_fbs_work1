#WAP to check given number is strong number

#Input number
num=int(input("Enter the number:"))

temp=num
sum_fact=0

#check each digit
while(temp>0):
    digit=temp%10

    #find factorial of digit
    fact=1
    for i in range(1, digit+1):
        fact=fact*i

    sum_fact=sum_fact+fact
    temp = temp//10

    #condition 
if(sum_fact==num):
        print("Strong number.")

else:
        print("Not a strong number.")

