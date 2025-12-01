'''
╔══════════════════════════════════════════════════════════════════════════════╗
║                                  PROJECT 07                                  ║
║                            EMPLOYEE INTAKE PROGRAM                           ║
╚══════════════════════════════════════════════════════════════════════════════╝ 

┌─── PROJECT 07 ─────────────────────────────┐   
│  Matthew Ochoa          CLASS: COSC 1336   │   
│ ┌────────────────────────────────────────┐ |   
| │           DATE: Nov 30, 20             | |   
│ │         STATUS: In-Progress            | |   
| └────────────────────────────────────────┘ |   
└────────────────────────────────────────────┘    

┌─── PROCEDURE ───────────────────────────────────────────┐   
│ ┌────────────────────────────── CORE: Requirements ───┐ |   
| │  GET:          Input Variables          <(1)        | |   
│ │  GENERATE:     Derived Variables        <(2)        | |   
│ │  DISPLAY:      Entry Form               <(3)        | |  
| └─────────────────────────────────────────────────────┘ |   
└─────────────────────────────────────────────────────────┘          

___────────────────────────────────────────────────────────────___
___──────────────────── DOCUMENTATION ─────────────────────────___
___────────────────────────────────────────────────────────────___

| REQUIREMENTS | 

    | INPUT - VARIABLES |

        Prompt | Input Variables
            last name
            first name
            SSN
            dependents
            wage
            employee ID

            
    | DERIVED - VARIABLES |

        Generate | Derived Variables

            initials            | first[:1] + last[:1] + .upper
            email               | first[:1] + last + @example.com
            l4ssn               | ssn[-4:]
            wage:float          | displayed as (f"${wage:.2f}")
            dependents          | 0-10 (inclusive)
            eID                 | (f"{last}.{l4ssn}")
    
    | REQUIRED - FUNCTIONS |

        getStringData()
            Validate non-empty
            returns validated
            
        getFloatData()
            Validate | wage > 0
            return validated

        getIntegerData()
            Validate | dependents >= 0
            return validated

        displayResult(varList):
            for key in list:
                ...

        validateSSN(ssn)
            Validate | format xxx-xx-xxxx 
            Validate | SSN is a 9-digit int

            Returns TRUE if valid and FALSE if not.
                - If TRUE, the last 4 digits of the SSN are extracted and displayed in main(). 
                - If FALSE, the user is prompted to re-enter the SSN.

        main() Orchestrates

        menu() | provideMenuFlow
            menu flow deliverable:
                offer choice to customize email domain
                    "Allow flexibility in formatting the email domain (optional input or preset constant)."
    | DISPLAY |

        Entry Title: Get a random job position from list
            offer choice to customize

        Domain: Get a random domain from list
            offer choice to customize
            
________________________________________________________________________
─────────────────────────────────────────────────────────────────────'''
#########################################################################
##                         PROVIDED FUNCTIONS                          ##
#──────────────────────────────────────────────────────────────────────##
#                     ** With Custom Validation **                      #
#-----------------------------------------------------------------------#

# This function will return an integer input from the user
# if Getting Dependents: Validate | dependents >= 0
def getIntegerData(prompt, isDependents):
    while (True):
        try:
            value = int(input(prompt))
            if isDependents:
                if value >=0:
                    return value
                else:
                    print("\tMust provide a # between 0 - 10!")
            else:
                return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a float input from the user
# if getting wage: Validate | wage > 0
def getFloatData(prompt, isWage):
    while (True):
        try:
            value = float(input(prompt))
            if isWage:
                    if (value >0):
                        return value
                    else:
                        print('\tNOT A VALID WAGE!')
                    
            else:
                return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')


# Validate non-empty | returns validated
def getStringData(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if value != '':
                return value
            else:
                print("\tProvide an INPUT!")
        except:
            print("\tProvide a Valid INPUT!")

# Returns single char input | validates 'W', 'D', or 'E'
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

#   SOPB - Start of Program Banner
#  ------------------------------------------------------------------------
def projectStart():
    print('\n',' ' * 4, '-'* 80, '\n',' ' * 4, 'Start of Project 07')
    print(' ' * 5, 'Written by: Matthew Ochoa')
    print(' ' * 5,'Date: 11/30/2025 ')
    print(' ' * 4,'-' * 80)
    print('\t  Form Design Program | Employee Intake Form')
    print(' ' * 4,'-' * 80, '\n')


#   EOPB - End of Program Banner
#  ------------------------------------------------------------------------
def projectEnd():
    print(' ' * 4,'-' * 80, '\n')
    print( ' ' * 5, 'End of Project 07')
    print(' ' * 4,'-' * 80)    

#   Validate SSN Format (xxx-xx-xxxx or 9 digits)
#  ------------------------------------------------------------------------
def validateSSN(prompt):
    while True:
        value = getStringData(prompt)  # Get SSN input <
        
        # Check numeric format (9 digits)
        if value.isnumeric():
            if len(value) != 9:
                print("\tUnsupported length for numerical format SSN input!")  # Error >
            else:
                return value  # Valid 9-digit SSN >
        
        # Check dashed format (xxx-xx-xxxx)
        elif '-' in value:
            if len(value) != 11:
                print("\tUnsupported length for SSN xxx-xx-xxxx format!")  # Error >
            elif value[3] != '-' or value[6] != '-':
                print("\tInvalid format! Use xxx-xx-xxxx format!")  # Error >
            else:
                return value  # Valid dashed SSN >
        else:
            print('\tPROVIDE VALID SSN!')  # Error: invalid format >

#   Store Input Variable in Dictionary
#  ------------------------------------------------------------------------
def getInputVars(vars:dict[object],name:str, value:object):
    vars.update({name:value})  # Add/update key-value pair |
    return vars  # Return updated dict >


#   Generate Derived Variables (initials, email, l4ssn, eID)
#  ------------------------------------------------------------------------
def generateDerived(vars:dict[object], domain):
    # Create initials from first and last name
    initials:str = (f"{(vars['first'])[:1]}{(vars['last'])[:1]}").upper()  # |
    
    # Generate email: firstInitial + lastName @ domain
    email:str = (f"{(vars['first'])[:1]}{vars['last']}@{domain}").lower()  # |
    
    # Extract last 4 SSN digits (remove dashes if present)
    ssn_clean = vars['ssn'].replace('-', '')  # Clean SSN |
    l4ssn:str = ssn_clean[-4:]  # Get last 4 digits |
    
    # Generate employee ID: lastName.last4SSN
    eID:str = (f"{vars['last'].lower()}.{l4ssn}")  # |
    
    # Store all derived variables
    vars.update({'initials':initials})
    vars.update({'email': email})
    vars.update({'l4ssn':l4ssn})
    vars.update({'eID': eID})
    
    return vars  # Return updated dict >

#   Menu - Collect Employee Input with Optional Customization
#  ------------------------------------------------------------------------
def menu(vars:dict[object]):
    # Set default values
    role = 'Software Developer'  # Default job title |
    domain = 'gmail.com'  # Default email domain |
    
    # Optional customization prompt
    while True:
        getIn = input('\n\tWould you like to change special values?\n\t\'y\' to modify: ')  # <
        if (getIn == 'y' or getIn == 'Y'):
            domain = input('\tProvide domain in (domain.com) format: ')  # <
            role = input('\tProvide your employee position: ')  # <
        break
    
    # Display data entry form header
    print()
    print(' ' * 4 + role + '\'s Entry')
    print(' ' * 4 + '-' * 80)
    print(' ' * 4 + 'Employer Information')
    
    # Collect all employee information
    last:str = getStringData(' ' * 8 + 'Last name    ')  # <
    vars = getInputVars(vars, 'last', last)  # Store |
    first:str = getStringData(' ' * 8 + 'First name    ')  # <
    vars = getInputVars(vars, 'first', first)  # Store |
    ssn:str = validateSSN(' ' * 8 + 'SSN (ex. 111-23-3333):  ')  # <
    vars = getInputVars(vars, 'ssn', ssn)  # Store |
    dependents:int = getIntegerData(' ' * 8 + 'Number of dependents: ', True)  # <
    vars = getInputVars(vars, 'dependents', dependents)  # Store |
    wage:float =  getFloatData(' ' * 8 + 'Wage: $', True)  # <
    vars = getInputVars(vars, 'wage', wage)  # Store |
    
    # Store customization options
    vars.update({'domain':domain})
    vars.update({'role':role})
    
    return vars  # Return complete input dict >


#   Display Employee Information Summary
#  ------------------------------------------------------------------------
def displayResults(vars):
    # Display formatted summary report
    print()
    print(' ' * 4 + '-' * 80)
    print(' ' * 4 + 'Summary: Create Identity')
    print(' ' * 4 + '-' * 80)
    print(' ' * 4 + 'The Employer\'s')
    print(' ' * 8 + f'Name:   {vars["first"]} {vars["last"]}')  # >
    print(' ' * 8 + f'User\'s initial:   {vars["initials"]}')  # >
    print(' ' * 8 + f'Email address:  {vars["email"]}')  # >
    print(' ' * 8 + f'Last 4-digit of SSN:  {vars["l4ssn"]}')  # >
    print(' ' * 8 + f'Number of dependents: {vars["dependents"]}')  # >
    print(' ' * 8 + f'Wage: ${vars["wage"]:.2f}')  # >
    print(' ' * 8 + f'Employee ID: {vars["eID"]}')  # >
    print()

#   MAIN FUNCTION - Program Orchestration
#  ------------------------------------------------------------------------
def main(): 
    vars:dict[object] = {}  # Initialize employee data dictionary |
    
    # Display program start banner
    projectStart()
    
    # Collect all employee input data
    vars = menu(vars)  # <
    
    # Generate derived variables (initials, email, eID, etc.)
    vars = generateDerived(vars, vars['domain'])  # <
    
    # Display formatted employee summary
    displayResults(vars)  # >
    
    # Display program end banner
    projectEnd()


#   PROGRAM ENTRY POINT
#  ------------------------------------------------------------------------
main()