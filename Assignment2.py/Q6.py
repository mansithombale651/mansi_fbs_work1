#WAP to calculate total salary of employee based on basic, da=10% basic, ta=12% of basic , hra=15% of basic

#input basic salary
basic_sal=int(input("Enter the basic salary:"))

#calculate allowances
da=0.10*basic_sal
ta=0.12*basic_sal
hra=0.15*basic_sal

#calculate total salary

total_salary=basic_sal+da+ta+hra

#Display output
print("Basic salary:",basic_sal)
print("DA(10%):",da)
print("TA(12%):",ta)
print("HRA(15%):",hra)
print("Total salary :", total_salary)

