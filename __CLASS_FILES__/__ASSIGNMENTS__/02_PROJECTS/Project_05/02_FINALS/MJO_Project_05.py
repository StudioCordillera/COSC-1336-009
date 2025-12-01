###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   November 25, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|   REQUIREMENTS - Project 05                                |
|   Objectives: Driver Distance Report                       |
|____________________________________________________________|

INPUTS (User Provided):
    - Vehicle speed (mph, must be > 0)
    - Travel time (hours, must be > 0)

PROCESSING:
    - Validate speed and time are positive
    - Calculate distance for each hour of travel
    - Formula: distance = speed × time
    - Generate hourly distance report

DISPLAY:
    - Table showing each hour and cumulative miles traveled
    - Column headers: "Hour" and "Miles Traversed"
    - One row per hour from 1 to total travel time

FUNCTIONS:
    - projectStart(): Display program header
    - projectEnd(): Display program completion message
    - getIntegerData(prompt): Get validated integer input
    - getFloatData(prompt): Get validated float input
    - getStringData(prompt): Get string input
    - getCharData(prompt): Get validated character input
    - shenanigans(): Validate speed and time inputs
    - calcParameters(speed, time): Calculate distance traveled
    - printSummary(): Display formatted distance report table
    - main(): Program orchestration

VALIDATION RULES:
    - Speed must be > 0 mph
    - Time must be > 0 hours
    - Error messages for invalid inputs
    - Re-prompt until valid input received

OUTPUT FORMAT:
    - Tabular display with aligned columns
    - Dynamic column spacing based on data
    - Shows distance for each hour incrementally

______________________________________________________________
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

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

#   SOPB
#  ------------------------------------------------------------------------
def projectStart():
    print(' ' * 4, '-'* 80, '\n',' ' * 4, 'Start of Project 5')
    print(' ' * 5, 'Written by: Matthew Ochoa')
    print(' ' * 5,'Date: 11/25/2025 ')
    print(' ' * 4,'-' * 80)
    print('\t  Driver Report | Get trip report from user inputs')
    print(' ' * 4,'-' * 80)


#   EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print(' ' * 4,'-' * 80, '\n')
    print( ' ' * 5, 'End of Project')
    print(' ' * 4,'-' * 80)
    
    
#   Validate Speed and Time Inputs
#  ------------------------------------------------------------------------
def shenanigans():
    # Display input section header
    print(f"\t{' ' * 5} Driver\'s Entry")
    print('\t',' ' * 3,'-' * 71)
    
    # Validate both inputs are positive
    while True:
        vehicleSpeed = getIntegerData(f"\t{' ' * 5} What is the speed of the vehicle in mph: ")  # <
        totalTravelTime = getIntegerData(f"\t{' ' * 5} How many hours has it traveled? ")  # <
        
        if (vehicleSpeed <= 0):
            print('\t\tYOU CANT BE GOING BELOW 1mph!!')  # Error: invalid speed >
        elif (totalTravelTime <= 0):
            print('\t\tBREAKING THE SPEED OF LIGHT NOT ALLOWED!!')  # Error: invalid time >
        else:
            break  # Valid inputs |
    
    return vehicleSpeed, totalTravelTime  # Return validated inputs >


#   Calculate Distance Traveled
#  ------------------------------------------------------------------------
def calcParameters(speed, time):
    distance = speed * time  # Calculate miles traveled |
    return distance  # Return distance >


#   Display Distance Report Table
#  ------------------------------------------------------------------------
def printSummary(vehicleSpeed, totalTravelTime):
    # Display summary header
    print('\n\t',' ' * 3,'-' * 71)
    print(f"\t{' ' * 5} Summary: Distance Traveled")
    print('\t',' ' * 3,'-' * 71)
    
    # Create table header with dynamic spacing
    banner = (' ' * 14)  + 'Hour '+ (' ' * 8) + 'Miles Traversed'
    print(f"\n{banner}")
    print('\t' + (' ' * 5) + ('-' * (len(banner)- 12)))
    
    # Display distance for each hour
    for hours in range(1, totalTravelTime + 1):
        distance = calcParameters(vehicleSpeed, hours)  # Calculate hourly distance <
        print('\t', ' ' * 5, hours, ' ' * (len(banner)-(28 + len(str(totalTravelTime)))), distance)  # Display row >
    print('\n')
    return
    
    
    
    
#   MAIN FUNCTION - Program Orchestration
#  ------------------------------------------------------------------------
def main(): 
    # Display program start
    projectStart()
    
    # Get validated speed and time inputs
    vehicleSpeed, totalTravelTime = shenanigans()  # <
    
    # Display distance report table
    printSummary(vehicleSpeed, totalTravelTime)  # >
    
    # Display program end
    projectEnd()


#   PROGRAM ENTRY POINT
#  ------------------------------------------------------------------------
main()


