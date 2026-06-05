#WAP to accept an integer amount from user and tell minimum number of notes needed for representing that amount

#Input amount
amount=int(input("Enter the amount:"))

#Calculate notes
note_500= amount//500
amount= amount% 500

note_200= amount//200
amount= amount% 200

note_100= amount//100
amount= amount% 100

note_50= amount//50
amount= amount% 50

note_20= amount//20
amount= amount% 20

note_10= amount//10
amount= amount% 10

note_5= amount//5
amount= amount% 5

note_2= amount//2
amount= amount% 2

note_1= amount//1
amount= amount% 1

#Display result
print("Minumum number of notes:")
print("500=", note_500)
print("200=", note_200)
print("100=", note_100)
print("50=", note_50)
print("20=", note_20)
print("10=", note_10)
print("5=", note_5)
print("2=", note_2)
print("1=", note_1)
