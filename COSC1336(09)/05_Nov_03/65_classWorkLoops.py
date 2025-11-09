########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 65                 #####
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

    # Display 10 - 30, increment by 5


    # for ctr in range of 10 - (-1)
    for ctr in range (10, 31, 5):
        print(ctr)

    
    # Display end of project
    projectEnd()
 
main()

# TRACE: 


