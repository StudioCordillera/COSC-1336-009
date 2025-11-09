########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 71                 #####
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

    while (True):
        try:
            # Prompt/get integer value
            value = int(input(prompt))
        
            # Send to main Integer data
            return value
        
        except ValueError:
            
            # Inform of error
            print('\t\tFucked Up')

# This function gets user entry for float
def getFloatData(prompt):

    while(True):
        try:
            
            # Prompt/get float
            value = float(input(prompt))
        
            # Send to main float value
            return value
        
        except ValueError:

            # Inform of error
            print('\t\tEnter a float type datatype!')

# This function gets user string input
def getStringData(prompt):
        value = input(prompt)

        # Send to main string value
        return value


# This function gets user string input
def getCharData(prompt):

    while (True):
        
        value = input(prompt).upper()

        if (value in ['Y', 'N']):
            
            # Send to main string value
            return value
        
        else:
            
            print('\tYou did not provide an acceptable answer')



########################################################################

def main():
    
    # Display start of project
    projectStart()

    dividend = getIntegerData('\tEnter dividend: ')

    divisor = getIntegerData('\tEnter divisor: ')

    try:
        result = dividend / divisor

        print('\tThe result is: ', result)

    except ZeroDivisionError:
        print('\t\tError MSG! Cannot divide by Zorro!')

    


    # Display end of project
    projectEnd()
 
main()

# TRACE: 


