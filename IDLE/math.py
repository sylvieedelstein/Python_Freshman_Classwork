#math.py
#Math expressions
#Sylvie Edelstein
#9/16/22
import math
def math_one():
    print (4.0 / 10.0 + 3.5 * 2)
    print (10 % 4 + 6 / 2)
    print (abs(4 - 20 // 3) ** 3)
    #square root causes an error because of attempting to square a negative
    print (3 * 10 // 3 + 10 % 3)
    print (3 ** 3)
math_one()

def math_two():
    for i in range(1, 11):
        print(i*i)

    for i in [1,3,5,7,9]:
        print(i, ":", i**3)
    print(i)

    x=2
    y = 10
    for j in range(0, y, x):
        print(j, end="")
        print(x + y)
    print("done")

    ans = 0
    for i in range(1, 11):
        ans = ans + i*i
        print(i)
    print (ans)

math_two()

def math_three():
    price = eval(input("How much did your pizza cost? "))
    diameter = eval(input("What is the diameter of your pizza? "))
    area = (diameter / 2) ** 2 * math.pi
    pizza_per_inch = round(price / area, 2)

    print ("The price of your pizza per square inch is ", pizza_per_inch)

math_three()

def math_four():
    height = eval(input("What is the height of your building? "))
    angle = eval(input("What is the angle of your ladder? "))

    radian = 180 * angle / math.pi
    length = height / math.sin (radian)

    print ("The length of your ladder is ", length)

math_four()
