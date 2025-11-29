# ----------------------------
# Ally Baba
# November, 2025
# Classwork #149
# ----------------------------
# Project Objectives
#   Learning OOP
# --------------------------------

from myFunctions import projectStart, projectEnd, getIntegerData, getStringData

class Friends:
    def __init__(self):
        self.name = None
        self.income = None

    # setters
    def setName(self, eValue):
        self.name = eValue

    def setIncome(self, eValue):
        self.income = eValue

    # getters
    def getName(self):
        return self.name

    def getIncome(self):
        return self.income

def main():
    
    # Display start of project
    projectStart()

    # object
    myFriends = Friends()

    name = getStringData('\tWhat is your name?: ')
    income = getStringData('\tWhat is your income?: $')

    myFriends.setName(name)
    myFriends.setIncome(income)

    print('\tName: ', myFriends.getName())
    print('\tIncome: $', myFriends.getIncome())

    # Display end of project
    projectEnd()

    
main()

# Trace:








