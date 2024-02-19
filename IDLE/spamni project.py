#Sylvie Edelstein
#9/30/22
#This program prompts the user for an input, prints the first letter of each word in the phrase, and converts each character to upper case.

def prompt():
    sentence = input("Enter a sentence! ")
    titlesentence = sentence.title()
    list1 = titlesentence.split()
    msg = ""
    for word in list1:
        msg = msg + word[0]
    print ('The acronym is', msg)
    

prompt()
