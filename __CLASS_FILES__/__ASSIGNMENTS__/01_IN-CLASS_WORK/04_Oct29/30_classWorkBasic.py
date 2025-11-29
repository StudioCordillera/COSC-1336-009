########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 30                 #####
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
    value = float(input(prompt))

    # Send to main hoursWorked
    return value


# This function gets user entry for float
def getFloatData(prompt):
    value = float(input(prompt))

    # Send to main hoursWorked
    return value

def main():
    # Display start of project
    projectStart()

    # Assign variable
    print('\tUser entry')
    myAge = getIntData('\tEnter your age: ')
        
    # Multiplying hours worked

    # Call Summary
    print('\tAge is: ', myAge)

    # Display end of project
    projectEnd()



          
main()

# Trace: 2
