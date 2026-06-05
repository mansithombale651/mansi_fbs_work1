#convert the time entered in hh , min , sec into seconds

#input Time from users
hours= int(input('Enter hours='))
minutes= int(input('Enter minutes='))
seconds= int(input('Enter seconds='))

#calculate total seconds
Total_seconds=(hours*3600)+(minutes*60)+seconds

#Display output
print("Total Seconds=",Total_seconds)