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
    print('\t  PROGRAM NAME | PURPOSE')
    print(' ' * 4,'-' * 80, '\n')

# Display End of Program Boiler EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print(' ' * 4,'-' * 80, '\n')
    print( ' ' * 5, 'End of Project')
    print(' ' * 4,'-' * 80)    

    
# function header
#  ------------------------------------------------------------------------


###############################################################
##    MAIN FUNCTION                                          ##
###############################################################

def main(): 
    # Calls function to display the start of project
    projectStart()

    # Below we start coding

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()



'''
 NOTES: dashes * 80 for meta data, 76 for program content
__________________________________________________________________

    OBJECT ORIENTED PROGRAMMING
__________________________________________________________________


          | UML DIAGRAM SPEC |
    _________________________________
    |                               |
    |   CLASS DEF                   |
    |_______________________________|
    |                               |
    |    DATA ATTRIBUTES            |
    |_______________________________|
    |                               |
    |   METHODS                     |
    |_______________________________|


__________________________________________________________________


    ______________________________
    | OPP - COFIG/MAP | UML SPEC | 
    |        ** INFORMAL **      |
    ------------------------------


    | CLASS DEF |
    ------------------------------


        | __DUNDERS__ |



    | DATA ATTRIBUTES |
    ------------------------------



    | METHODS |
    ------------------------------


        | ACCESSORS |


        | MUTATORS |


    ------------------------------


__________________________________________________________________


| OPP - IMPORTS |


| OPP - ## |


| OPP - ## |


| OPP - ## |


__________________________________________________________________


Overview 
    - User inputs:
        - last name
        - first name
        - social 
        - dependents #
        - wage
        - employee ID

    - Generates
        - initials
            - The user's initials (first letter of first name + first letter of last name)

        - email
            - The user's email address in the format: <first initial><lastname>@domain.com
                - (May use placeholder domain - @example.com)

        - l4SSN
            - The last 4 digits of the SSN

        - wage
            - The wage if formatted 2 decimal places with a $ sign

        - dependents
            - The number of dependents is between 0 and 10 (inclusive)

        - eID
            - The employee ID is the last name, a dot and the last 4 digits of SSN

    - Displays all variables
        - As seen in example

REQUIRED FUNC:
    - getStringData()
        - Validates: non-empty(str)
        - returns: validated user input

    - getFloatData()
        - Validates: input>0
        - returns: wage

    - getIntegerData()
        - Validates: input>=0
        - returns: dependents #

    - validateSSN()
        - Takes arguement: SSN entry
        - Validates: format (xxx-xx-xxxx)
        - Returns TRUE=valid + FALSE=INVALID
        
        (TRUE - the last 4 digits of the SSN are extracted and displayed in main())
        (FALSE - the user is prompted to re-enter the SSN)

    - displayResult()
        - Takes: values
        - Displays: final output
            - initials, email, and the last 4 digits of the SSN. 

    - main()
        - Controls the overall program logic. 
 
Optional Enhancements 
    - Validate: SSN = 9 digit
    - Allow flexibility in formatting the email domain (optional input or preset constant)

Programming Style Requirements 
    - Use meaningful variable names
    - Follow standard code formatting practices
    - Include documentation at the beginning of the file and above each function
 
  
__________________________________________________________________


| REQUIREMENTS | 

| FILE STANDARDS |

| STATIC - VARIABLES |

| INPUT - VARIABLES |

| DYNAMIC - VARIABLES |

| DISPLAY |

| FUNCTIONS |

_______________________________________________________

  OUTPUT PREVIEW
____________________


Project #7 
Written by: Ally Baba 
----------------------------------------------- 
 
 
    Lottery Commissioner's Entry 
    -------------------------------------------------------------------------------- 
    Employer Information 
        Last name    Smith 
        First name    John 
        SSN (ex. 111-23-3333):  123-45-5678 
        Number of dependents: 2 
        Wage: $10.00 
    
    -------------------------------------------------------------------------------- 
    Summary: Create Identity  
    -------------------------------------------------------------------------------- 
    The Employer's 
        Name:   John Smith 
        User's initial:   JS 
        Email address:  jsmith@gmail.com 
        Last 4-digit of SSN:  5678 
        Number of dependents: 2 
        Wage: $10.00 
        Employee ID: smith.5678 
    
    -------------------------------------------------------------------------------- 
    End of Project 7 

'''