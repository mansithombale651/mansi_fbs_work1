n= int(input("Enter the number :"))
fact=1
sum_series=0

for i in range(1,n+1):
    fact= fact*i
    sum_series +=i/fact

print("Sum of series =",sum_series)