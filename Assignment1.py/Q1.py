#WAP to print the percentage of student based on marks of any 5 students

# take input
m1= int(input('enter 1st students marks:'))
m2= int(input('enter 1st students marks:'))
m3= int(input('enter 1st students marks:'))
m4= int(input('enter 1st students marks:'))
m5= int(input('enter 1st students marks:'))

#perform operation
gain_marks=m1+m2+m3+m4+m5
perc=gain_marks/500*100

#display output
print(f'Percentage of 5 subject is=', perc)