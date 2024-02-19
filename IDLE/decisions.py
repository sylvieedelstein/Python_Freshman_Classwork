#Sylvie Edelstein
#decisions.py
#10/18/22

def decisions():
    n = int(input("Number? "))
    if n < 0:
        print("The absolute value of ", n, "is", -n)
    else:
        print("The absolute value of", n, "is", n)


decisions()


def elif_statement():
    a = 0
    while a <10:
        a = a + 1
        if a > 5:
            print(a, ">", 5)
        elif a <= 3:
            print (a, "<=", 3)
        else:
            print("Neither test was true")
elif_statement()

def high_low():
    number = 7
    guess = -1

    print("Guess the number!")
    while guess != number:
        guess = int(input("Is it..."))

        if guess == number:
            print ("Hooray! You guess it right!")
        elif guess < number:
            print ("It's bigger...")
        elif guess > number:
            print ("It's not so big.")
        

high_low()

def even():
    number = float(input("Tell me a number: "))
    if number % 2 == 0:
        print(int(number), "is even.")
    elif number % 2 == 1:
        print (int(number), "is odd.")
    else:
        print(number, "is very strange.")
even()

def average():
    count = 0
    sum = 0.0
    number = 1

    print("Enter 0 to exit the loop")

    while number != 0:
        number = float(input("Enter the number: "))
        if number != 0:
            count = count + 1
            sum = sum + number
        if number == 0:
            print ("The average was:", sum / count)
average()
