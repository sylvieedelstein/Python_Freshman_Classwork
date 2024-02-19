def addInterest(balance, interest_rate):
    newBalance = balance * (1 + interest_rate)
    return newBalance

def test():
    amount = 1000
    rate = 0.05
    newAmount = addInterest(amount, rate)
    print(newAmount)

addInterest()
test()
