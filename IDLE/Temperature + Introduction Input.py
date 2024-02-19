def main():
    for i in range(5):
        print ("This programs converts a temperature in Celsius to one in Fahrenheit!")
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.")


main()
