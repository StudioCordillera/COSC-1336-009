# Ally Baba
# November, 2025
# Classwork #89
# ----------------------------
# Project Objectives
#   Learning Lists
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tLearning Lists")
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
    value = input(prompt).strip(' ')

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

def main():
    # Display start of project
    projectStart()

    #element# 1   2   3   4    5    6   7
    myList = [23, 44, 100, 33, 129, 75, 23] # List
    #index    0   1    2    3   4     5  6 left to right
    # index                             -1 right to left

    print('\tMy original List: ', myList)

    # slicing a list
    print('\tStarts @ index(3) | Ends @ end of list', myList[3:]) # [33, 129, 75, 23]
    print('\tStarts @ index(5) | Ends @ end of list', myList[5:]) # [75, 23]

    print('\tStarts @ index(10) | Ends @ end of list', myList[10:]) #

    print('-' * 60)
    print('\tStarts @ index(beginning) | Ends @ (index - 1) ', myList[:3]) # [23, 44, 100]
    
    print('\tStarts @ index(beginning) | Ends @ (index - 1) ', myList[:4]) # [23, 44, 100, 33]

    print('-' * 60)
    print('\tStarts @ index(2) | Ends @ (4) ', myList[2:5]) # [100, 33, 129]
    print('\tStarts @ index(1) | Ends @ (2) ', myList[1:3]) # [44, 100]
    
    # Display end of project
    projectEnd()
   
main()

# Trace:








