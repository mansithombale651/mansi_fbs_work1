#WAP To find the root of quadratic equation

#take input
a= float(input("Enter value of a:"))
b= float(input("Enter value of b:"))
c= float(input("Enter value of c:"))

#perform operation
d=(b**2-(4*a+c))**0.5
root_1=(-b+d)/2**a
root_2=(-b-d/2**a)

#display output
print("root 1=", root_1)
print("Root 2=", root_2)