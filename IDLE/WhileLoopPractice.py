#whilelooppractice.py
#Sylvie Edelstein
#10/28/22
#This code experiments with while loops

def looptest1():

    number = 7
    while number < 20:
        print("Nice!")
        if number%5 == 0:
            print("The number "+str(number)+" is divisible by five")
        else:
            print("The number "+str(number)+" is not divisible by five")

        number = number + 1



def looptest2():
    for number in range(5):
        print("Nice!")



def looptest3():
    for number in range(5):
        print("teehee")
        print("I am outer loop iteration "+str(number))
        for number2 in range(5):
            print("heehee")
            print("I am inner loop iteration "+str(number2))

looptest1()
looptest2()
looptest3()

def looptest4():
    n = 5
    for i in range(5):
        for j in range(i):
            print('* ', end="")
        print('')

looptest4()

def looptest5():
    number = 7
    while number < 20:
        print("Nice!")
        if number%5 == 0:
            print("The number "+str(number)+" is divisible by five")
            break

        number = number + 1

looptest5()

def looptest6():
    number = 7
    while number < 20:
        print("Nice!")
        if number%5 == 0:
            print("The number "+str(number)+" is divisible by five")
            break
        
        #continue

        number = number + 1


looptest6()



    
