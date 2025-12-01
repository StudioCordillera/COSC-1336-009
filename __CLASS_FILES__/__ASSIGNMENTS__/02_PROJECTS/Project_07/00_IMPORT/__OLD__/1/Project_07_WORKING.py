########################################
## Matthew Ochoa                   #####
## MONTH ##, #yr#                  #####
## Project: ##                     #####
## Status: In - Progress           #####
## Class: COSC 1336                #####
########################################
# ------------------------------------------------------------#
#  Compny Accounts Manager | Uses Forms for Employee records  #
# ------------------------------------------------------------#
#                | Project 3 - Requirements |                 #
# ------------------------------------------------------------#
'''



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
    print('\t  New Employee form ')
    print(' ' * 4,'-' * 80, '\n')

# Display End of Program Boiler EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print(' ' * 4,'-' * 80, '\n')
    print( ' ' * 5, 'End of Project')
    print(' ' * 4,'-' * 80)    


# function header
#  ------------------------------------------------------------------------
def validateSSN(prompt):

    while True:

        ssn = getStringData(prompt)

        if ssn.isalpha == True:
                print('\tENTER SSN ONLY!')

        try:
            if (len(ssn) < 9):
                print('\tProvide full SSN')

            if (len(ssn) == 9 and ssn.isnumeric() == True):
                ssn1, ssn2, ssn3 = ssn[:3], ssn[3:5], ssn[5:]

                ssn = None
                ssn = f"{ssn1+ '-'+ ssn2+  '-'+ ssn3}"
            return ssn
        except:
            print('\t\tFOLLOW REQUESTED FORMAT!!')

def shenanigans():
    varType = type(inputVal)
    if varType == int:
        if inputVal <1:
            print('\tINPUT must be positive!')
    elif varType == float:
        if inputVal < 1:
            print('\tINPUT must be positive!')
        else:
            inputVal = f"{inputVal:.2f}"
            return inputVal
    else:
        inputVal = inputVal.lower().strip()
        return inputVal
        

# function header
#  ------------------------------------------------------------------------
def dataOrchestration():
   
        # function header
    #  --------------------------------------------------------------------
    while True:
        try:
            SSN = validateSSN('\tSSN (ex. 111-23-3333): ')
            last = shenanigans(getStringData('\tLast name: '))
            first = getStringData('\tFirst name: ')
            dependents = getIntegerData('\tNumber of dependents: ')
            wage = getIntegerData('\twage: $')

        except:
                

    initFirst, initLast, l4SSN, eID, emailAddr = buildVarDepends(last,first,  SSN)
    varList1 = [initFirst, initLast, l4SSN, eID, emailAddr]
    varList = [last, first, dependents, wage, SSN]
    varList = varList + varList1
       
    return varList
        

# function header
#  ------------------------------------------------------------------------
def buildVarDepends(last, first, SSN):

    stfirst = str(first).lower()
    stlast = str(last).lower()
    initFirst = stfirst[:1].upper()
    initLast = stlast[:1].upper()
    stSSN = str(SSN).replace('-','')
    l4SSN = stSSN[5:]
    eID = str(f"{last,l4SSN}")
    emailAddr = initFirst, last, '@python.alibaba.com'
    name = first,' ',last

    return  initFirst, initLast, l4SSN, eID, emailAddr, name


# function header
#  ------------------------------------------------------------------------
def displayResult(varList):



    spacingKey = "(' '* 12), ' * 'Number of dependents: "
    spacing = int(len(spacingKey)/2)

    print('\n', ' ' * 4,'-' * 80)
    print('\t  Summary: Create Identity ')
    print(' ' * 4,'-' * 80)
    print('\t  The Employer\'s')
    print((' '* 12), 'Name: ', ' '*spacing, name)
    print((' '* 12), 'User\'s initial:  ', ' '*spacing, initials,)
    print((' '* 12), 'Email address: ', ' '*spacing, emailAddr)
    print((' '* 12), 'Last 4-digit of SSN: ', ' '*spacing, l4SSN)
    print((' '* 12), 'Number of dependents: ', ' '*spacing, dependents)
    print(f"{(' '* 12), 'Wage: ', ' '*spacing, wage}")
    print((' '* 12), 'Employee ID: ', ' '*spacing, eID)




    
###############################################################
##    MAIN FUNCTION                                          ##
###############################################################

def main(): 
    # Calls function to display the start of project
    projectStart()

    varList = dataOrchestration()
    print(varList)

    displayResult(varList)

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()

