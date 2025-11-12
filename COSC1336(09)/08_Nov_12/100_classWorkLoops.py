########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
#### Classwork N. 95               #####
## --------------------------------#####
## Project Objectives              #####
##   Learning Lists                #####
########################################################################

# This function will display the start of project
def projectStart():
    print('\n', "-" * 60, '\n\n\tStart of Project'+ '\n\tWritten By Matthew Ochoa' + '\n\tLearning Lists' + '\n\n' + "-" * 60, '\n')

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


'''
# This function will get user entry for an integer ####################
def getInteger2Data(prompt):

    while (True):
        try:
            # Prompt/get integer value
            value = int(input(prompt))
        
            # Send to main Integer data
            if (value <= 5 and value >= 1):
                return value

            else:
                print('\tEnter a value between 1 and 5!')
        
        except ValueError:
    
            # Inform of error
            print('\t\tFucked Up')
'''


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
        value = input(prompt).strip(' ')

        # Send to main string value
        return value


# This function gets user string input
def getCharData(prompt):

    while (True):
        
        value = input(prompt).upper()

        if (value in ['B', 'C', 'X']):
            
            # Send to main string value
            return value
        
        else:
            
            print('\tYou did not provide an acceptable answer')



def listFunc(myList):

    print('\tMy origional list: ', myList)

    count23s = myList.count(23)

    print('\tHow many 23\'s in myList?: ', count23s)



########################################################################



def main():
    
    # Display start of project
    projectStart()

    # My List
    myList = [23, 44, 23, 33, 23, 75, 23]

    # Run List Function
    listFunc(myList)


    # Display end of project
    projectEnd()
 
main()

# TRACE: 


