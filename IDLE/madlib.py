#madlib.py
#This is a mad libs program!
#Sylvie Edelstein
#9/13/22

def main():
    print("This program lets you play a game of mad libs! Enter the required words as they appear.")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    print("The", adjective, noun, verb, "through the giant", place, ".")
    playing = input("Do you want to continue playing? Enter 'Yes' or press any key to stop playing ")
    if playing == "Yes":
            main()
    else:
        print("Thank you for playing! Press the <Enter> key to quit.")
main()

    
