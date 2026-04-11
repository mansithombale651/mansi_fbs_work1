n = int(input ("Entr the number of employee:"))
total_emp=0

for i in range(1,n+1):
    basic_sal=float(input("Enter basic salary of employee{i}:"))

    if(basic_sal<20000):
        da=0.10*basic_sal
        ta=0.12*basic_sal
        hra=0.15*basic_sal

    else:
        da=0.15*basic_sal
        ta=0.18*basic_sal
        hra=0.20*basic_sal

    total_salary=(basic_sal + da+ ta+ hra)
    total_emp=(total_emp+ total_salary)
    print("Total salary of employee=",total_salary)

print("total salary of all employees=",total_emp)



        

