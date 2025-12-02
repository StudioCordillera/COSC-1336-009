# --------------------------------
# Ally Baba
# November, 2025
# Classwork #163
# --------------------------------
# Project Objectives
#   Learning OOP
# every time i walk i advance 5 miles
# --------------------------------

from myFunctions import projectStart, projectEnd, getIntegerData, getStringData

class Walking:
    def __init__(self, eName, eMiles): # Constructors
        self.name = eName
        self.milesWalk = eMiles

    def getMilesWalk(self):
        return self.milesWalk

    def getName(self):
        return self.name

    def setMilesWalk(self, eValue):
        self.milesWalk = eValue
        
    def setName(self, eName):
        self.eName = eName

    def walkMile(self):
        self.milesWalk = self.milesWalk + 2

    def walkBack(self):
        self.milesWalk = self.milesWalk - 1

        if (self.milesWalk < 0):
            self.milesWalk = 0



def main():
    # Display start of project
    projectStart()

    name = getStringData('\tEnter Your Name: ')
    value = getIntegerData('\tEnter Your Miles: ')

    myWalking = Walking(name, value)

    # myWalking.setName(name)
    # myWalking.setMilesWalk(value)

    print('\tName: ', myWalking.getName())
    print('\tMiles Walked: ', myWalking.getMilesWalk())

    value = getIntegerData('\tHow many times have you Walked?: ')



    for ctr in range(value):
        myWalking.walkMile()

    print('\tNew Miles Walked: ', myWalking.getMilesWalk())


    

    
    # Display end of project
    projectEnd()
   
main()

# Trace:








