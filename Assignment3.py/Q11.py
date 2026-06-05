#Accept age of five people and also per person ticket amount and then calculate total 
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

total_amount=0
for i in range(1,6):
    age=int(input(f"Enter age of person {i }:"))

    ticket=float(input(f"Enter ticket amount for person {i}:"))

    #apply condition
    if(age<12):
        discount=0.30*ticket
        final_amount=ticket-discount

    elif(age>59):
        discount=0.50*ticket
        final_amount=ticket-discount

    else:
        final_amount= ticket

    total_amount=total_amount+ final_amount

print("Total ticket amount for all person:",total_amount)