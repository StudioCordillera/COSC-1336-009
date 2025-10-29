########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 31                 #####
## --------------------------------#####
## Project Objectives              #####
##   Learning the basics of Python #####
########################################

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By Matthew Ochoa")
    print("\tLearning Functions")
    print("-" * 60)

# This fucntion will display the end of project
def projectEnd():
    print('\n')
    print('-' * 60)
    print('\tEnd of project')

# This function will get user entry for an integer
def getIntData(prompt):
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
    myAge = getIntData('\tEnter your age: ')
    myName = getStringData('\tEnter your name: ')
    
    # Multiplying hours worked

    # Call Summary
    print('\tAge is: ', myAge)
    print('\tName is: ', myName)

    # Display end of project
    projectEnd()



          
main()

# Trace: 2
