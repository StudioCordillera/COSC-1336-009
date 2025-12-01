########################################
## Matthew Ochoa                   #####
## MONTH ##, #yr#                  #####
## Project: ##                     #####
## Status: In - Progress           #####
## Class: COSC 1336                #####
########################################

import OOP_EMPLOYEE_CLASS


# ------------------------------------------------------------#
#                | Project 3 - Requirements |                 #
# ------------------------------------------------------------#


# TODO | Include documentation at the beginning of the file and above each function


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

    



    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()




##################################################################
'''




company domain + company name | will be a configurable global variable changeable from a menu settings feature

Global (within employee repository class)
	domain

From: (Validated Input)
	First
	Last
	Dependents
	Wage
	SSN

From: (Generated using Input vars)
	Initials
	Email
	Last 4 SSN
	Employee ID

Formatting Requirements:

domain (str) | domain.com | domain extension validation (exists?) + (in list of common?)

First (str).lower()
Last (str).lower()
Dependents (int) | Range: 0-10 (inclusive)
Wage (int) | Wage Formatted (str) = (f"${int}")
SSN (int) = xxxxxxxxx | SSN Formatted (str) = (f"{SSN[:3]+'-'SSN[3:4]+'-'+SSN[5:]}") = xxx-xx-xxxx | input could be xxxxxxxxx (str(int)), xxx-xx-xxxx (str) need to be validated and stored as (int) then a formatted version as mentioned.

Initials (str) | (f"{fname[0:]+lname[0:]}").upper() = FL
Email (str) | (f"{fname[0:]+lname+'@'+domain}")
Last 4 SSN | (f"{SSN[5:]}")
Employee ID | (f"{lname+'.'+l4SSN}")



OOP_APP_CLASS.py
----------------------------


> Start program

    > Main Menu

        Choose an option:

        	r. Register New Employee
        	m. Manage Employees Collection
        	c. Change Company Settings
        	e. exit

    > option r. New Employee
        > 1. Get input

            Provide First Name:
            	~

            Provide Last Name:
            	~

            Provide # of Dependents for Employee: (0-10)
            	~

            Provide SSN of Employee:
            	~

            Provide Employee Wage:
            	~

        > 1.1 Check input

            Provided Employee Info: (enter # to change 1)

            	1. First Name: ~
            	2.  Last Name: ~
            	3. Dependents: ~
            	4. 	  SSN: ~
            	5. 	 Wage: ~

            Choose Option:

            	#. Change selected item
            	a. Change all items
            	f. Finalize Employee In-Take
            	c. Cancel New Employee Registration

        > 1.2 Finalize Employee In-Take

            Employee Info
        
                Initials
                Last, First
                SSN
                Dependents
                Wage

                1. Email
                2. eID

            Choose Option:

            	#. Manually edit fields
            	f. Finalize Employee
            	c. Cancel Registration
        
    > Option m. Manage Employee Collection

        > 2 Show list of Employees

            Company Name | Domain.com
            _____________________________
            eID | Employee
            ...

        Provide an eID to manage an employee: (or c to cancel)
            ~

        > 2.1 Edit employee | eID provided

            Choose an option:

            	e. Edit Employee Info
            	a. Archive Employee
            	d. Delete Employee
            	c. Cancel


            > 2.2 Option e. Edit Employee info

                1. Initials
                2. Last
                3. First
                4. SSN
                5. Dependents
                6. Wage

                7. Email
                8. eID

                Choose Option:

                	#. Manually edit fields
                	a. Finalize Employee
                	c. Cancel Employee Edit

            > 2.2 Option a. Archive Employee

                Are you sure you want to ARCHIVE eID: lName, fName?

                	y. Yes, archive employee
                	c. Cancel

            > 2.3 Option d. Delete Employee

                Are you sure you want to DELETE eID: lName, fName?

                	y. Yes, delete employee
                	c. Cancel

    > Option c. Change company info

        > Company Info Menu

            1. Company Name
            2. Domain

            Choose an option:

            	#. edit item
            	c. Cancel

    > Option 3.1 Change Company Name

        Insert new company name:
        	~
    
        Company Name will be changed from (old name) to (new name).
    
        Choose an option:
    
        	a. Apply changes
        	e. Edit New Company Name
        	c. Cancel

    > Option 3.2 Change Company Domain

        Insert new Domain:
        	~

    > Option 3.2 [case 1: domain extension not recognized OR format issues]

        Company Domain will be changed from (old domain) to (new domain).

        Warning: Domain extension not recognized.
        {and/or} : Warning: Format does not match standard (domain.com) format.

        Choose an option:

        	a. Apply Changes
        	e. Edit New Domain
        	c. Cancel

    > Option 3.2 [case 2: domain extension recognized, no format issues]

        Company Domain will be changed from (old domain) to (new domain).

        Choose an option:

        	a. Apply Changes
        	e. Edit New Domain
        	c. Cancel














__________________________________________________________________


OOP CLASSES:
    1 | EMPLOYEE_CLASS
    2 | EMPLOYEE_REPOSITORY_CLASS
    3 | APP_CLASS

1 | EMPLOYEE CLASS

    Contains all employee object variables for items in the repo


2 | EMPLOYEE REPOSITORY CLASS

    manages employee objects repository

    any adding, revising, deleting of items in repo


3 | APP CLASS

    provides a menu experience and functionality for other classes





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


| OPP - IMPORTS > MAIN |


| OPP - Classes |


| OPP - Class - Dunders |


| OPP - Class - Accessors |

| OPP - Mutators |

| OPP - Class  |

__________________________________________________________________


| REQUIREMENTS | 

| FILE STANDARDS |

| DYNAMIC - VARIABLES |

| INPUT - VARIABLES |

    - last name
        - Validates: non-empty(str)

    - first name
        - Validates: non-empty(str)

    - social 
        - Validates: format (xxx-xx-xxxx)

    - dependents #
        - Validates: input>=0

    - wage
        - Validates: input>0


| DEPENDENT - VARIABLES |

    - initials
        - The user's initials (first letter of first name + first letter of last name)

    - email
        - The user's email address in the format: <first initial><lastname>@domain.com
            - (May use placeholder domain - @example.com)
            - Allow flexibility in formatting the email domain (optional input or preset constant)

    - l4SSN
        - The last 4 digits of the SSN

    - wage
        - The wage = $0.00 format

    - dependents
        - The number of dependents is between 0 and 10 (inclusive)

    - eID
        - The employee ID = last name + dot + last 4 digits of SSN


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


    

__________________________________________________________________

OLD FUNCTIONS REQUIREMENTS
__________________________________________________________________


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
        - Validates
            - format (xxx-xx-xxxx)
            - SSN = 9 digit
        - Returns TRUE=valid + FALSE=INVALID
            - (TRUE - the last 4 digits of the SSN are extracted and displayed in main())
            - (FALSE - the user is prompted to re-enter the SSN)

    - displayResult()
        - Takes: values
        - Displays: final output
            - initials, email, and the last 4 digits of the SSN. 

    - main()
        - Controls the overall program logic. 
 __________________________________________________________________

'''