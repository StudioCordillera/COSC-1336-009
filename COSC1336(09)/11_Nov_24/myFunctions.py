# ----------------------------
# Ally Baba
# November, 2025
# Classwork #149
# ----------------------------
# Project Objectives
#   Learning OOP
# --------------------------------

# class:identifier starts capital
class Rectangle:
    def __init__(self, eLength, eWidth):
        self.length = eLength
        self.width = eWidth

    # getters
    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    # setters
    def setLength(self, eValue):
        self.length = eValue

    def setWidth(self, eValue):
        self.width = eValue

    # method to find area
    def findArea(self):
        return self.length * self.width

    def findPerimeter(self):
        return 2 * self.length + 2 * self.width
    
# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tLearning OOP")
    print("-" * 60)

# This function will display the end of project
def projectEnd():
    print('\n')
    print('-' * 60)
    print('\tEnd of project')

# This function will get the user's entry for a float
def getFloatData(prompt):
    while (True):
        try:
            
            value = float(input(prompt))

            return value

        except ValueError:
            print('\t\tERRor MSG! Non numbers entered')

# This fucntion will get the user's entry for an integer
def getIntegerData(prompt):

    while (True):
        try:
            value = int(input(prompt))
            return value

        except ValueError:
            print('\t\tERRor MSG! Non numbers entered')

# This function will get the user's entry of string
def getStringData(prompt):
    value = input(prompt).strip(' ')

    return value

# This function will get a char input
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()

        if (value in ['Y', 'N']):
            return value
        else:
             print('\t\tERRor MSG! Enter Y | N')
   


# Trace:








