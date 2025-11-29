# Ally Baba
# November, 2025
# Classwork #71
# ----------------------------
# Project Objectives
#   Learning Loops
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tLearning Loops")
    print("-" * 60)

# This fucntion will display the end of project
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

            if (value >= 1 and value <= 5):
                return value
            else:
                print('\t\tError MSG! Enter values between 1 and 5')

        except ValueError:
            print('\t\tERRor MSG! Non numbers entered')

# This function will get the user's entry of string
def getStringData(prompt):
    value = input(prompt).rstrip(' ')

    return value

# This function will get a char input
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()

        if (value in ['B', 'C', 'X']):
            return value
        else:
             print('\t\tERRor MSG! Enter B | C | X')

# This function will display a menu
def mainMenu():
    print('-' * 60)
    print('\tAlly Baba Booger Shop')
    print('-' * 60)
    print('\tB       Booger Burger')
    print('\tC       Chicken Buger')
    print('\tX       Exit')
    print('-' * 60)

def main():
    # Display start of project
    projectStart()

    name = getStringData('\tEnter your name: ')

    print('\tMy name is: ', name)
    
    # Display end of project
    projectEnd()
   
main()

# Trace:








