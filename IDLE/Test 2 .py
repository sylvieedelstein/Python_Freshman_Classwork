#Sylvie Edelstein
#November 8th, 2022
#TestQuestion9.py
#This program gets info from the user about how they want their mattress delivered

def delivery():
     print("This program will ask you two questions about your purchase, and give you its total cost.")
     print("")
     price = 0
     mattress = input("Which mattress would you like to purchase? Type T for Twin, Q for Queen, and K for King: ").lower()
     if mattress == "t":
          price = price + 150
     elif mattress == "q":
          price = price + 200
     elif mattress == "k":
          price = price + 275
     else:
          print("Sorry, but this is not a type of mattress we sell.")


     shipping = input("What delivery method would you like? Type P for Pickup, R for Regular, and E for Express: ").lower()
     if shipping == "p":
          price = price + 0
     elif shipping == "r":
          price = price + 30
     elif shipping == "e":
          price = price + 70
     else:
          print("Sorry, but we do not offer this kind of shipping service.")
     
     price = round(price, 2)
     print("Your total is: $", price)
     print("")
     print("Thank you for using our service.")
     input("Press Enter to exit") 
     
          
delivery()
          
     

