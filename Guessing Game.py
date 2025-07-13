#Guessing secret number


secret_number=9
guess_limit=3
i=0
while i<guess_limit:
    guess_number=int(input("Guess: "))
    i = i + 1
    if secret_number == guess_number:
        print("You won!")
        break

else:
    print("Wrong Guess!")
    print(f'Actual secret number is: {secret_number} ' )