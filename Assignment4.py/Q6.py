#WAP to check if a given number is prime or not

num=int(input("Enter the number:"))

if( num<= 1):
    print("Not a prime number.")

else:
    for i in range(2, int(num**0.5) +1):
        if(num%i==0):
            print("Not a prime number.")
            break
    else:
        print("prime number")

  
