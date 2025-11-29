########################################
## Matthew Ochoa                   #####
## MONTH ##, #yr#                  #####
## Project: ##                     #####
## Status: In - Progress           #####
## Class: COSC 1336                #####
########################################
#  TITLE OF PROGRAM | DESC
# ------------------------------------------------------------#
#                | Project 3 - Requirements |                 #
# ------------------------------------------------------------#

'''| Objectives | 
    
    Core:
        1) Get
        2) Operate
        3) Print
        
'''

###############################################################
##                    PROVIDED FUNCTIONS                     ##
###############################################################

# This function will return an integer input from the user
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a float input from the user
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

# This function will return a string input from the user
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()
        if (value in ['W', 'D', 'E']):
            return value

        print('\t\tERROR Message: Wrong selection')
        
###############################################################
##                      START - MY CODE                      ##
###############################################################

# Display Start of Program Boiler SOPB
#  ------------------------------------------------------------------------
def projectStart():
    print(' ' * 4, '-'* 80, '\n',' ' * 4, 'Start of Project 4')
    print(' ' * 5, 'Written by: Matthew Ochoa')
    print(' ' * 5,'Date: 11/25/2025 ')
    print(' ' * 4,'-' * 80)
    print('\t  Driver Report | Get trip report from user inputs')
    print(' ' * 4,'-' * 80)

# Display End of Program Boiler EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print(' ' * 4,'-' * 80, '\n')
    print( ' ' * 5, 'End of Project')
    print(' ' * 4,'-' * 80)
    
    
#  VALIDATION FUNC
# ------------------------------------------------------------------------
def shenanigans():
    
    # Style
    print(f"\t{' ' * 5} Driver\'s Entry")
    print('\t',' ' * 3,'-' * 71)


    while True:
        vehicleSpeed = getIntegerData(f"\t{' ' * 5} What is the speed of the vehicle in mph: ")
        totalTravelTime = getIntegerData(f"\t{' ' * 5} How many hours has it traveled? ")
        
        if (vehicleSpeed <= 0):
            print('\t\tYOU CANT BE GOING BELOW 1mph!!')
        elif (totalTravelTime <= 0):
            print('\t\tBREAKING THE SPEED OF LIGHT NOT ALLOWED!!')
            
        else:
            break
        
    return vehicleSpeed, totalTravelTime


#  PROCESS INPUTS
# ------------------------------------------------------------------------
def calcParameters(speed, time):
    

    distance = speed * time

    return distance


#  SUMMARY PRINT FUNC
# ------------------------------------------------------------------------s
def printSummary(vehicleSpeed, totalTravelTime):
    print('\n\t',' ' * 3,'-' * 71)
    print(f"\t{' ' * 5} Summary: Distance Traveled")
    print('\t',' ' * 3,'-' * 71)
    banner = (' ' * 14)  + 'Hour '+ (' ' * 8) + 'Miles Traversed'
    print(f"\n{banner}")
        
    print('\t' + (' ' * 5) + ('-' * (len(banner)- 12)))
    
    for hours in range(1, totalTravelTime + 1):
        print('\t', ' ' * 5, hours, ' ' * (len(banner)-(28 + len(str(totalTravelTime)))),  calcParameters(vehicleSpeed,hours))
    print('\n')
    return
    
    
    
    
###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 
    # Calls function to display the start of project
    projectStart()

    # call validation func
    vehicleSpeed, totalTravelTime = shenanigans()
    
    # print summary
    printSummary(vehicleSpeed, totalTravelTime)

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()


