########################################
## Matthew Ochoa                   #####
## November 17, 2025               #####
#### Classwork N. 119              #####
## --------------------------------#####
## Project Objectives              #####
##   Learning Strings              #####
########################################################################

# This function will display the start of project
def projectStart():
    print('\n')
    print( "-" * 60, '\n\n\tStart of Project'+ '\n\tWritten By Matthew Ochoa' + '\n\tLearning Lists' + '\n\n' + "-" * 60, '\n')

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


    
'''

    SSN = getStringData('\tEnter your SSN (xxx-xx-xxxx): ')

    # Conditions: 9 characters
    # 2 dashes

    if (len(SSN)!= 11):
        print('\t', SSN, ' is not valid SSN')
    else:
        if(SSN.count('-')!=2 or SSN[3]!='-' or SSN[6]!='-'):
            print('\t', SSN, ' is not valid SSN')
        else:
            if (SSN.replace('-','').isdigit()):
                print('\tEntered : ', SSN)
            else:
                print('\t', SSN, ' is not valid SSN')
    


'''

########################################################################



def main():
    
    # Display start of project
    projectStart()


    python = [1, 3, 4, 88, 98, 1]
    math = [2, 1, 3, 4, 56, 99, 2]

    print('\tPython student list: ', set(python))
    print('\tMath student list: ', set(math))   

    
    # Display end of project
    projectEnd()
 
main()

# TRACE: 


