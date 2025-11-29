########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 81                 #####
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



########################################################################



def main():
    
    # Display start of project
    projectStart()

    # Count Numbers
    countNumbers = 0
    sumNumbers = 0
    averageNumbers = 0

    # object
    try:
        
        fileRead = open('data1.txt', 'r')

        for line in fileRead:
            line = line.strip('\n').strip(' ')

            try:
                value = int(line)
            
                print('\tThe value is: ', value)

                countNumbers = countNumbers + 1
                sumNumbers = sumNumbers + value

                
            except ValueError:
                continue
        
        fileRead.close()
        print('\tCount of Numbers: ', countNumbers)
        print('\tSum of Numbers: ', sumNumbers)
        
        
        if (countNumbers == 0):
            print('\tNo data!')
        else:
            averageNumbers = sumNumbers/countNumbers # calc avg
            print('\tAverage of Numbers: ', format(averageNumbers, '.2f'))


        
    except FileNotFoundError:
        print('\tFile not found!!')

    


    # Display end of project
    projectEnd()
 
main()

# TRACE: 


