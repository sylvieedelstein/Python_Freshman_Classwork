#Sylvie Edelstein
#username.py
#10/7/22
#This program creates username

def username():

    print("This program asks for your first and last name and creates a username")
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    user = first_name[0].lower() + last_name[:7].lower()

    print("Your username is", user)

username()
