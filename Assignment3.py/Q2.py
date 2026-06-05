#WAP to input any alphabet and check whether it is vovel or consonant

alphab= str(input('Enter the alphabet:'))

if alphab in(['a','e','i','o','u','A','E','I','O','U']):
    print("This is the vovel.")

else:
    print('This is the consonant')