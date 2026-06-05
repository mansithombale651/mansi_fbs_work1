#WAP to swap two numbers using third variable

#input two numbers
a=int((input("Enter first number:")))
b=int((input("Enter second number:")))

print("Before swapping:")
print("a=",a)
print("b=",b)

#Swapping using third variable
temp=a
a=b
b=temp

print("After swapping:")
print("a=",a)
print("b=",b)
