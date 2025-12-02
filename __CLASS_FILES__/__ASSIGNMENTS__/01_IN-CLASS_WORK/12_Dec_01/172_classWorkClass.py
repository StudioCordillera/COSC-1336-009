# ----------------------------
# Ally Baba
# November, 2025
# Classwork #163
# ----------------------------
# Project Objectives
#   Learning OOP
# --------------------------------

from myFunctions import projectStart, projectEnd, getIntegerData, getStringData

class Walking:
    def __init__(self, eName, eMiles): # Constructors
        self.name = eName
        milesWalk = eMiles

    def getMilesWalk(self):
        return self.milesWalk

    def getName(self):
        return self.eName

    def setMilesWalk(self, eValue):
        self.milesWalk = eValue
    def setName(self, eName):
        self.eName = eName



def main():
    # Display start of project
    projectStart()

    name = getStringData('\tEnter Your Name: ')
    value = getIntegerData('\tEnter Your Miles: ')

    myWalking = Walking(value, name)

    # myWalking.setName(name)
    # myWalking.setMilesWalk(value)

    print('\tName: ', myWalking.getName())
    print('\tMiles Walked: ', myWalking.getMilesWalk())

    
    # Display end of project
    projectEnd()
   
main()

# Trace:








