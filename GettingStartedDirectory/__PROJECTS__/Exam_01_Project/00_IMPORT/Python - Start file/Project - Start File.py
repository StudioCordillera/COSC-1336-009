# ---------------------------------------------
# Name: Your Name
# Date: Date of sunmission
# Project: Eam 1 Project 
# Status: WIP
# Class: COSC 1336
# ---------------------------------------------
# Description
#   Here you write the project desctiptiopn
# ---------------------------------------------

# This function will display the start of the project
def projectStart():
    print('Start of Exam 1 Project ')
    print('Written by: Your Name')
    print('Date: Enter date ')
    print('-' * 50 )
    print('\tHere your write project information')
    print('-' * 50 + '\n')

# This function will display the start of the project
def projectEnd():
    print('-' * 50)
    print('End of Exam 1 Project')

# This function will return an integer input from the user
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a float input from the user
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

# This function will return a string input from the user
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()
        if (value in ['W', 'D', 'E']):
            return value

        print('\t\tERROR Message: Wrong selection')

def main(): 
    # Calls function to display the start of project
    projectStart()

    # Below we start coding

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()


