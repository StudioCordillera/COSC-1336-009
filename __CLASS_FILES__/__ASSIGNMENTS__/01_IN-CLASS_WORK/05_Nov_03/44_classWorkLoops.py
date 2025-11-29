########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 44                 #####
## --------------------------------#####
## Project Objectives              #####
##   Learning Loops                #####
########################################

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By Matthew Ochoa")
    print("\tLearning Loops")
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

    # Call while loop
    # Stop Watch | Set 0 (by default)
    # Increment i by 1 ever iteration
    stopWatch = 0

    while(stopWatch<5):
        print(stopWatch, '\tMy name is Matthew Ochoa')
        stopWatch=stopWatch +1
        

    # Display
    
    # Average Grades

    # Call Summary

    # Display end of project
    projectEnd()
 
main()


