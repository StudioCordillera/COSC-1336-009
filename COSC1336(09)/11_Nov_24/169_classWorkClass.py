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
    def __init__(self, eName, eIncome):
        self.name = eName
        self.income = eIncome

        # derived member
        self.status = selfFindRichPeople()


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

    def getStatus(self):
        return self.status

    # methods
    def findRichPeople(self):
        if (self.income > 1000000):
            return "You are my Friend!!"
        else:
            return "GET LOST PEASANT!!"


def main():
    
    # Display start of project
    projectStart()


    name = getStringData('\tWhat is your name?: ')
    income = getIntegerData('\tWhat is your income?: $')

    # object
    myFriends = Friends(name, income)


    print('\tName: ', myFriends.getName())
    print('\tIncome: $', myFriends.getIncome())
    print('\tStatus: ', myFriends.getStatus())

    # Display end of project
    projectEnd()

    
main()

# Trace:








