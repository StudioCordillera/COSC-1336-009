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
    def __init__(self, eMiles): # Constructors
        milesWalk = eMiles

    def getmilesWalk(self):
        return self.milesWalk

    def setmilesWalk(self, eValue):
        self.milesWalk = eValue



def main():
    # Display start of project
    projectStart()

    value = getIntegerData('\tEnter Your Miles: ')

    myWalking = Walking()

    myWalking.setMilesWalk(value)

    print('\tMiles Walked: ', myWalking.getMilesWalk())

    
    # Display end of project
    projectEnd()
   
main()

# Trace:








