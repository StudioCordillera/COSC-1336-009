
'''
 NOTES: dashes * 80 for meta data, 76 for program content
__________________________________________________________________


| STATIC - VARIABLES |

    name        |   first + last
    initials    |   1st char of (first, last)
    emailAddr   |   1st name init + Last + @domain.com
    last4       |   derived by SSN
    eID         |   last+last4
    
| STATIC - VARIABLES - SPEC |

    initials (FL) 
        - (1st of First) + (1st of Last)
    email address (FLast@domain.com) 
        - <first initial><lastname>@example.com. 
    last 4 
        - of SSN. 
    Wage 
        - 2 decimal places 
        - $ sign
    dependents #  0 
        - 10 (inclusive) 
    The employee ID 
        - last name.(last 4)

| INPUT - VARIABLES |

      last  | last name
      first | first name
      SSN   | Social Security Number (SSN)
 dependents | number of dependents
       wage | wage
        eID | employee ID

| OOP |

    Each object Stored in .txt file in company folder dir for employees

    class = employee
    data attributes | self.attribbute = variable | self.__4SSN = str(SSN)[:4]

        # PUBLIC
            last
            first
            inFirst
            inLasTt

        # SECRETS BELOW
            __SSN
            __4SSN
            __dependents
            __wage
            __eID
            __emailAddr
    

    accessors = [
    
    ]
    
    mutators = [
    
    ]

    User EXP Menu

| VALIDATION |

    • SSN = 9-digit number. 
    • Robust email capture
        - flexibility
            - formatting - email domain 
            - optional input, preset constant
     

| FUNCTIONS + REQUIREMENTS(FUNC) | 

    validateSSN()
        - Validates
            - format
                (xxx-xx-xxxx)
        - Returns
            - TRUE if valid
                - Last 4 processed
                - return Last 4 => main
            - FALSE if not
                - re-prompt user
                    - SSN 

    getInput():
        - INPUT ORCHESTRATION AND VALIDATION ASSURANCE

    buildVarDepends():
        - Contstructs variables for which are dependent on others presence

    getMenu():
        - deploys an interactive menu for user operations 

    storeObject():
        - stores class as file version in directory, handles naming
    
    getObject():
        - loads class object as file in directory, and initializes state from creation instance menu


    displayResult()
    - Accepts
        - required values
        
    Displays
        - final outputs
            - initials
            - email
            - last 4


    main() | ORCHESTRATION

| DISPLAY |

    JOB TYPE | BANNER
        - JOB TITLE'S ENTRY

    FORM DESC BANNER + PAIRS
        - 'Employer Information'


    Lottery Commissioner's Entry
    
             LABEL | VALUE      
         Last name | Smith      
        First name | John       
               SSN | 123-45-5678
        dependents |  2         
              Wage | $10.00     
    
    ADMINISTRATOR VERSION OF THE FORM | POST: SIGN-UP
    -------------------------------------------------------------------------------- 
    Summary: Create Identity  
    -------------------------------------------------------------------------------- 
                   ? - might be too much formatting work
    ---------------|--------------
    |        LABEL | VALUE        |
    |    Last name | Smith        |
    |   First name | John         |
    |          SSN | 123-45-5678  | (ex. 111-23-3333)
    |   dependents |  2           |
    |         Wage | $10.00       |
    |______________|______________|

    The Employer’s 
     Name:   John Smith 
    User’s initial:   JS 
    Email address:  jsmith@gmail.com 
    Last 4-digit of SSN:  5678 
    Number of dependents: 2 
    Wage: $10.00 
    Employee ID: smith.5678 

_______________________________________________________
    
      OUTPUT PREVIEW
________________________

    Project #7 
    Written by: Ally Baba 
    ----------------------------------------------- 
    
    
    Lottery Commissioner’s Entry 
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
    The Employer’s 
        Name:   John Smith 
        User’s initial:   JS 
        Email address:  jsmith@gmail.com 
        Last 4-digit of SSN:  5678 
        Number of dependents: 2 
        Wage: $10.00 
        Employee ID: smith.5678 
    
    -------------------------------------------------------------------------------- 
    End of Project 7
'''


# function header
#  ------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
# --------------------------------------------| STATIC - VARIABLES |-------------------------------------------
#   
#       domain = alibab.com
#       name = f"{first' 'last}"
#       1st = first[:3]
#       Lst = last[:2]}
#       initials = f"{1st' 'Lst}"
#       emailAddr = f"{1st+last+'@'+domain}"
#       last4 = SSN[:5]
#       eID = last+last4
#
# -------------------------------------------------------------------------------------------------------------
#
#       name |< first + last
#       initials |< 1st char of (first, last)
#       emailAddr |< 1st name init + Last + @domain.com
#       last4 |< derived by SSN
#       eID |< last+last4
#
# -------------------------------------------------------------------------------------------------------------
# ----------------------------------------| STATIC - VARIABLES - SPEC |----------------------------------------
#   
#       initials (FL) 
#           - (1st of First) + (1st of Last)
#       email address (FLast@domain.com) 
#           - <first initial><lastname>@example.com. 
#       last 4 
#           - of SSN. 
#       Wage 
#           - 2 decimal places 
#           - $ sign
#       dependents #  0 
#           - 10 (inclusive) 
#       The employee ID 
#           - last name.(last 4)
#                                             
#                        ---------------------| INPUT - VARIABLES|---------------------
#   
#       last = last name
#       first = first name
#       SSN = full SSN as ()
#       dependents = numercal
#       wages = hourly
#       eID = 
#   
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------| DYNAMIC - VARIABLES |------------------------------------------
#   
#       Identity template dictionary
#       Identies database file
#       User EXP Menu
# 
# -------------------------------------------------------------------------------------------------------------
