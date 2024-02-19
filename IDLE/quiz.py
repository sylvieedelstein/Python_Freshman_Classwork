#Sylvie Edelstein
#10/21/22
#quiz.py
#This program is a quiz that calculates the number of correct answers the user has

def quiz():
    print("This is a simple quiz testing your basic knowledge. All correct answers are one word or number. Do your best!")
    score = 0
    print("How many politicians are in the senate?")
    print("")
    print("a) 300")
    print("b) 200")
    print("c) 100")
    print("d) 50")
    question1 = input("Choose the correct letter: ").lower()
    if question1 == "c":
        score = score + 1
        print("Correct!")

    else:
        print("I'm sorry. That is not correct.")

    print("What color is featured in the center of the Japanese flag?")
    print("")
    print("a) yellow")
    print("b) white")
    print("c) blue")
    print("d) red")
    question2 = input("Choose the correct letter: ").lower()
    if question2 == "d":
        score = score + 1
        print("Correct!")

    else:
        print("I'm sorry. That is not correct.")

    print("Who composed 32 Sonatas in their lifetime?")
    print("")
    print("a) mozart")
    print("b) davinci")
    print("c) jason derulo")
    print("d) beethoven")
    question3 = input("Choose the correct letter: ").lower()
    if question3 == "d":
        score = score + 1
        print("Correct!")

    else:
        print("I'm sorry. That is not correct.")

    print("How many inches are in a foot? ")
    print("")
    print("a) 5")
    print("b) 12")
    print("c) 10")
    print("d) 8")
    question4 = input("Choose the correct letter: ")
    if question4 == "b":
        score = score + 1
        print("Correct!")

    else:
        print("I'm sorry. That is not correct.")

    print("What theory explains why jumping off a building would cause you to hit the ground?")
    print("")
    print("a) gravity")
    print("b) social darwinism")
    print("c) thermodynamics")
    print("d) the big bang")
    question5 = input("Choose the correct letter: ").lower()
    if question5 == "a":
        score = score + 1
        print("Correct!")

    else:
        print("I'm sorry. That is not correct.")

    if score > 4:
        print("Congratulations you are a certified G-E-N-I-U-S!")
    elif score == 3:
        print("You did pretty well. You aren't perfect, but not everyone can be me!")
    elif score == 4:
        print("You did pretty well. You aren't perfect, but not everyone can be me!")
    elif score < 3:
        print("I mean that was just tragic. I didn't know that was even possible.")

quiz()
    
