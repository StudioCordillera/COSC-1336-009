MONEY = 1

def addMoney():
    global MONEY
    MONEY = MONEY + 1

print ("Before function is called", MONEY)
addMoney()
print ("After function is called", MONEY)
