#WAP TO CONVERT DAYS INTO YEARS , WEEKS ,DAYS

#Take input 
days=int(input("Enter number of days:"))

#calculate year
years=days//365
days=days%365

#calculate weeks 
weeks= days//7
days= days%7

#display result
print("years:",years)
print("Weeks:",weeks)
print("days",days)