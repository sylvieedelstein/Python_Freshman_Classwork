#Sylvie Edelstein
#11/1/22
#quizwithloops.py
#This program is a quiz that loops until you get the right answer

def quiz():
    quizagain="y"
    while quizagain[0] == "y":
        print("This is a simple quiz testing your basic knowledge.")
        print("How many politicians are in the senate?")
        print("")
        print("a) 300")
        print("b) 200")
        print("c) 100")
        print("d) 50")
        correct = False
        while correct == False:
            question1 = input("Choose the correct letter or 's' to skip: ").lower()
            print("")
            if question1 == "c":
                print("Correct!")
                print("")
                correct = True
            elif question1=="s":
                print("The correct answer was 'c) 100'")
                print("")
                correct = True
            else:
                print("This is incorrect. Please try again.")
                print("")
        correct = False

        print("What color is featured in the center of the Japanese flag?")
        print("")
        print("a) yellow")
        print("b) white")
        print("c) blue")
        print("d) red")
        correct = False
        while correct == False:
            question2 = input("Choose the correct letter or 's' to skip: ").lower()
            print("")
            if question2 == "d":
                print("Correct!")
                print("")
                correct = True
            elif question2=="s":
                print("The correct answer was 'd) red'")
                print("")
                correct = True
            else:
                print("This is incorrect. Please try again.")
                print("")
        correct = False

        print("Who composed 32 Sonatas in their lifetime?")
        print("")
        print("a) mozart")
        print("b) davinci")
        print("c) jason derulo")
        print("d) beethoven")
        correct = False
        while correct == False:
            question3 = input("Choose the correct letter or 's' to skip: ").lower()
            print("")
            if question3 == "d":
                print("Correct!")
                print("")
                correct = True
            elif question3=="s":
                print("The correct answer was 'd) beethoven'")
                print("")
                correct = True
            else:
                print("This is incorrect. Please try again.")
                print("")
        correct = False

        print("How many inches are in a foot? ")
        print("")
        print("a) 5")
        print("b) 12")
        print("c) 10")
        print("d) 8")
        correct = False
        while correct == False:
            question4 = input("Choose the correct letter or 's' to skip: ")
            print("")
            if question4 == "b":
                print("Correct!")
                print("")
                correct = True
            elif question4=="s":
                print("The correct answer was 'b) 12'")
                print("")
                correct = True
            else:
                print("This is incorrect. Please try again.")
                print("")
        correct = False

        print("What theory explains why jumping off a building would cause you to hit the ground?")
        print("")
        print("a) gravity")
        print("b) social darwinism")
        print("c) thermodynamics")
        print("d) the big bang")
        correct = False
        while correct == False:
            question5 = input("Choose the correct letter or 's' to skip: ").lower()
            print("")
            if question5 == "a":
                print("Correct!")
                print("")
                correct = True
            elif question5=="s":
                print("The correct answer was 'a) gravity'")
                print("")
                correct = True
            else:
                print("This is incorrect. Please try again.")
                print("")
        correct = False

        quizagain = input("Would you like to play again? ").lower()
    print("Thank you for playing.")
    input("Press Enter to exit") 
            
quiz()
        

