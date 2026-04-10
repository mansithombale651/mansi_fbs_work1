# WAP to input two angle from user and find third angle of the triangle

#take input
angle1= float(input("Enter 1st angle:"))
angle2= float(input("Enter 2nd angle:"))

#perform operation
angle3=180-(angle1+angle2)

#display output
print('Third angle of the triangle is:',angle3)