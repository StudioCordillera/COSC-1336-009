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

    # setters
    def setName(self, eValue):
        self.name = eValue

    # getters
    def getName(self):
        return self.name

def main():
    
    # Display start of project
    projectStart()

    # object
    myFriends = Friends()

    name = getStringData('\tWhat is your name?: ')

    myFriends.setName(name)

    print('\tName: ', myFriends.getName())

    # Display end of project
    projectEnd()

    
main()

# Trace:








