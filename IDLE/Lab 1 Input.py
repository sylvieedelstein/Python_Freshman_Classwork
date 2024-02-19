print("Hello, world!")
print("Hello", "world!")
print(3)
print(3.0)
print(2 + 3)
print(2.0 + 3.0)
print("2" + "3")
print("2 + 3 =", 2 + 3)
print(2 * 3)
print(2 ** 3)
print(7 / 3)
print(7 // 3)

# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 2.0 * x * (1 - x)
        print(x)

main()

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)

main()

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    for i in range(10):
        x = 3.9 * (x - x * x)
        print(x)

main()

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    for i in range(10):
        x = 3.9 * x - 3.9 * x * x
        print(x)

main()

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    for i in range(10):
        x = 3.9 * x - 3.9 * x * x
        print(x)

main()






