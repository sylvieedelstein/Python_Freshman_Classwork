#Sylvie Edelstein
#date.py
#10/7/22
#This program finds the date

def date():
    print("This program asks for the date as a list and gives it to you as a sentence.")
    date_short = input("Give me the date in the format 'mm/dd/yyyy': ")
    date_list = date_short.split("/")
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    months = int(date_list[0])
    print ("The date selected is: " + month_list[months - 1], date_list[1] + ", " + date_list[2] + ".")
    
    
date()
