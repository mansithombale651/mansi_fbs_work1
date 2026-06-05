#WAP to calculate profit or loss 

#cp=cost price
#sp=selling price

cp=float(input('Enter cost price:'))
sp=float(input('Enter the selling price:'))

if(cp>sp):
    print('Loss.')

elif(sp>cp):
    print("Profit.")

else:
    print("NO profit no loss")