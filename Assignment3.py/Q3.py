#WAP to input angle of a triangle and check whether triangle is valid or not

#input angle
a=int(input('Enter first angle:'))
b=int(input('Enter second angle:'))
c=int(input('Enter third angle:'))

if(a+b+c==180 and a>0 and b>0 and c>0):
    print('The triangle is valid.')

else:
    print('The triangle is not valid.')