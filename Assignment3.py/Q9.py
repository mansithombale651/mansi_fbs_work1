#input 5 subjects mark from user and display grade(eg. first class, second class)

#input marks
m1= int(input('Enter mark of subject 1:'))
m2= int(input('Enter mark of subject 2:'))
m3= int(input('Enter mark of subject 3:'))
m4= int(input('Enter mark of subject 4:'))
m5= int(input('Enter mark of subject 5:'))

#perform operation
gain_marks=m1+m2+m3+m4+m5
percentage=gain_marks/500*100

#display percentage
print("Percentage:",percentage)

#check grade
if(percentage>=60):
    print("first class.")

elif(percentage >= 40):
    print("Second class.")

elif(percentage >= 20):
    print("Third class.")

else:
    print("Fail.")

