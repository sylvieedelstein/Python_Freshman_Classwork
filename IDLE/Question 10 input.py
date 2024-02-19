#Sylvie Edelstein
#November 8th, 2022
#TestQuestion10.py
#This program has the user guess a secret number

def secretnumber():
    print("This program will have you guess my secret number!")
    print("")
    guesses = 3
    while guesses > 0:
        number = input("Guess a number from 1 to 10: ")
        if number == "7":
            print("You guessed correctly!")
            break
        else:
            print("Sorry, that's incorrect.")
            guesses = guesses - 1
    else:
        print("Sorry. Game over.")
    print("")
    print("Thank you for playing!")
secretnumber()
    
