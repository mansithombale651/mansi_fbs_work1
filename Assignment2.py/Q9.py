#WAP to swap two numbers  without using third variable

#Take input
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))

print("Before swapping:")
print("a=",a)
print("b:",b)

#swapping without using 3rd variable
b=b-a
a=a+a


#Display output
print("After swapping a:{a}, y:{b}")
print("a=",a)
print("b=",b)


