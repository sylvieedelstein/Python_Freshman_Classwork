#Sylvie Edelstein
#10/18/22
#Payroll.py
#This algorithm calculates pay

def payroll():
    hours = float(input("How many hours have you worked? "))
    rate = float(input("What is your pay rate per hour? "))
    if hours <= 40:
        pay = hours * rate
        
    else:
        payrate = rate * 40
        overtime = hours - 40
        overtimepay = overtime * rate * 1.5
        pay = overtimepay + payrate
        
    pay = round(pay, 2)
    print ("Your total pay is", pay)

payroll()
