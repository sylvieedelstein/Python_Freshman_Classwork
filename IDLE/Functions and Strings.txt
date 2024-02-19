#Intro Programming
#Lab 8 - Working with Functions and Strings
#Sylvie Edelstein
#November 18, 2022

def getname():
    #get user's first and last names
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    return(firstName,lastName)

def createUserName (fname, lname):
    username=fname[0]+lname.lower()
    return(username)

def getpassword():

    #ask user to create a new password
    password = input("Create a new password: ")

    #TODO modify this to ensure the password has at least 8 characters
    while len(password) < 8:
        print("Fool of a Took! That password is feeble!")
        return False
    else:
        print("The force is strong in this one...")
        return True

def main():
    
    #TODO modify this to generate a Marist-style username
    first, last = getname()
    uname = createUserName(first, last)
    while True:
        if getpassword() == True:
            break
    print("Account configured. Your new email address is", uname + "@marist.edu")

main()
