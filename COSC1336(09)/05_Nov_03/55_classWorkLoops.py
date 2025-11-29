########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 53                 #####
## --------------------------------#####
## Project Objectives              #####
##   Learning Loops                #####
########################################################################

# This function will display the start of project
def projectStart():
    print("-" * 60, '\n\tStart of Project'+ '\n\tWritten By Matthew Ochoa' + '\n\tLearning Loops' + '\n' + "-" * 60)

# This fucntion will display the end of project
def projectEnd():
    print('\n' + '-' * 60, '\n\tEnd of project')

########################################################################
    

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


########################################################################

def main():
    # Display start of project
    projectStart()

    # Enter integers until 0
    # Display how many numbers have been entered
    # Display sum of numbers

    # init start watch vars
    counter = 1

    # Init accumulator
    sumNumbers = 0
    
    value = getIntegerData("\tEnter an integer. 0 will terminate: ")

    print('\tCounter of Iterations: ', counter)
    
    while (value != 0):

        # Add New input to Accumulator
        sumNumbers=sumNumbers+value

        
        # Update Loop
        value = getIntegerData("\tEnter an integer. 0 will terminate: ")



        # Increment counter + 1
        counter = counter + 1
        print('\tCounter of Iterations: ', counter)
        
    print('\tSum of Numbers: ', sumNumbers)
    # Display end of project
    projectEnd()
 
main()

# TRACE: 


