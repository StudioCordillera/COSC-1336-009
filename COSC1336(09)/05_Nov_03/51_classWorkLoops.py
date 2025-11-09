########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 51                 #####
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

    # Enter integers until -999
    # -999 is called SENTINEL
    # Check before loop
    # Pre_read & inside loop update-read

    value = getIntegerData("\tEnter an integer. -999 will terminate: ")

    
    while (value != -999):
        # Update Loop
        value = getIntegerData("\tEnter an integer. -999 will terminate: ")

 
    # Display end of project
    projectEnd()
 
main()

# TRACE: 0>63>43>45>52>55(?)>57 -> 55(?)>57(T)>55(-999)>57(F)>61


