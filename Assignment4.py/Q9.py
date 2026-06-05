#print all number in range divisible by a given number

start=int(input("Enter start number:"))
end=int(input("Enter end number:"))
num=int(input("Enter the number:"))

for i in range(start,end+1):
    if(i %num == 0):
        print(i)

    