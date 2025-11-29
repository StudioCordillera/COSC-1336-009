########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 36                 #####
## --------------------------------#####
## Project Objectives              #####
##   Learning IF's                 #####
########################################

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By Matthew Ochoa")
    print("\tLearning IF's")
    print("-" * 60)

# This fucntion will display the end of project
def projectEnd():
    print('\n')
    print('-' * 60)
    print('\tEnd of project')

# This function will get user entry for an integer
def getIntegerData(prompt):
        value = int(input(prompt))

        # Send to main Integer data
        return value

# This function gets user entry for float
def getFloatData(prompt):
        value = float(input(prompt))

        # Send to main float value
        return value

# This function gets user string input
def getStringData(prompt):
        value = input(prompt)

        # Send to main string value
        return value


def main():
    # Display start of project
    projectStart()

    # Assign variable
    print('\tUser entry')
    value = getIntegerData('\tEnter an integer: ')

    # Display if value even or odd
    if (value % 2 == 0):
        print('\tValue is EVEN')
    else:
        print('\tValue is ODD')
    
    
    # Average Grades

    # Call Summary

    # Display end of project
    projectEnd()
 
main()


