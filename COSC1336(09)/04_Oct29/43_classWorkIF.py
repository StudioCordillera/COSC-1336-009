########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 43                 #####
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
    numberChecks = getIntegerData('\tEnter number of checks: ')

    # Display
    # write checks
    # more than 40 checks > pay .10; more than 20; pay .15 otherwise pay .20
    
    if (numberChecks >= 40):
        print('\tPay .10')
    elif (numberChecks >= 20):
        print('\tPay .15')
    else:
        print('\tPay .20')
    
    # Average Grades

    # Call Summary

    # Display end of project
    projectEnd()
 
main()


