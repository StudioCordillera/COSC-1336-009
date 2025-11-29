########################################
## Matthew Ochoa                   #####
## November 06, 2025               #####
## Project: 03                     #####
## Status: FINISHED                #####
## Class: COSC 1336                #####
########################################

# ------------------------------------------------------------#
#                | Project 3 - Requirements |                 #
# ------------------------------------------------------------#

''' 

    | Objectives | 
    
    Core:
        1) Prompts the user to enter the (month), and the (number of checks) written during such. 
        2) Calculates - total from (bank fees + flat fees) from input and calculations from given function.
        3) Displays the total monthly fees. 
    
    Additional:
        4) Validate the user's input (data-types)
        5) If negative number provided: (LOGIC)
            5.1) Display message: '<MessageHere>' <| MESSAGE NOT PROVIDED IN REQUIREMENTS DOC!! |
            5.2) DO NOT - perform calculation

    | LOGIC |
    
    (additionalFees) conditional logic:
        a) <20 checks: $0.10/check  
        b) 20-39 checks: $0.08/check  
        c) 40-59 checks: $0.06/check  
        d)  >= 60 checks: $0.04/check 

'''
###############################################################
##                    PROVIDED FUNCTIONS                     ##
###############################################################

# This function will return an integer input from the user
def getIntegerData(prompt):
    try:
        value = int(input(prompt))
    except ValueError:
        print('\tONLY INTEGERS!!')
    return value

# This function will return a float input from the user
def getFloatData(prompt):
    try:
        value = float(input(prompt))
    except ValueError:
        print('\tONLY NUMBERS!!')
    return value

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt).strip().lower().upper()
    return value

###############################################################
##                      START - MY CODE                      ##
###############################################################

# Display Start of Program Boiler SOPB
#  ------------------------------------------------------------------------
def projectStart():
    print('-' * 50 + '\n')
    print('Start of Project 3')
    print('Written by: Matthew Ochoa')
    print('Date: 11/06/2025\n')
    print('-' * 50 + '\n')
    print('\tBank Teller\'s Entry')
    print('\t', '-' * 50 + '\n')

# Display End of Program Boiler EOPB
#  ------------------------------------------------------------------------
def projectEnd():

    print('\tEnd of Project 3')
    print('-' * 50 + '\n')


# Calculate Check Fees Function
#  ------------------------------------------------------------------------
def calculateFees(monthIndex, checks):
    

    if (checks <20):
        bankFees = float(checks * .10)
    elif(checks <40):
        bankFees = float(checks * .08)
    elif(checks<60):
        bankFees = float(checks * .06)
    else:
        bankFees = float(checks * .04)
        
    flatFees = float(10 * monthIndex)

    totalFees = flatFees + bankFees

    return totalFees

# Get User input for
#  ------------------------------------------------------------------------
def getUserInput():
    
    month, checks, monthIndex = shenanigans()
            
    return month, checks, monthIndex

# Handle Shenanigans (validation and month key ID delegation) Function
#  ------------------------------------------------------------------------
def shenanigans():
    
    while True:
        try:
            month, monthIndex = monthHandler(getStringData('\tEnter the month: '))

        except IndexError:
            print('\tENTER A MONTH')

        break
        # validate not <0 condition

    while True:
        checks = getIntegerData('\tEnter the number of checks written this month? ')
        if checks >0:
            break
        else: 
            print('\tONLY POSITIVE INTEGERS!!')
        
    return month, checks, monthIndex
    
    
# Handle Months store key and value pair data in variables then return
#  ------------------------------------------------------------------------
def monthHandler(month):
    
    monthList = {
        1: ['JAN', 'JANUARY'],
        2: ['FEB', 'FEBUARY'],
        3: ['MAR', 'MARCH'],
        4: ['APR', 'APRIL'],
        5: ['MAY', 'MAY'],
        6: ['JU7', 'JUNE'],
        7: ['JUL', 'JULY'],
        8: ['AUG', 'AUGUST'],
        9: ['SEP', 'SEPTEMBER','SEPT',],
        10: ['OCT', 'OCTOBER'],
        11: ['NOV', 'NOVEMBER'],
        12: ['DEC', 'DECEMBER']
    }
    
    if (month.isnumeric() == True):
        try: 
            month = int(month)
        except ValueError:
            print('\tCHOOSE 01 OR Jan OR January FORMAT!!')
            
        if month in monthList:
            try:
                
                monthKey = monthList[month][1]
                monthValue = month
                
                return monthKey, monthValue
            except:
                print('\tINCORRECT FORMATTING')
        else:
            print('\tMUST BE A VALID MONTH AND FORMAT!!')
    else:
           
        for keys in monthList:
            if month in monthList[keys]:

                monthKey = monthList[keys][1]
                monthValue = keys

                return monthKey, monthValue
            
            
def printSummary(month, checks, totalFees):
    
    # Display Summary
    print('\n\t', '-' * 50)
    print('\tSummer: Bank')
    print('\t', '-' * 50)
    print(f'\tMonth of statement: {month}')
    print(f'\tFor writing {checks} checks, the bank fee is ${totalFees:.2f}.\n')
    print('\t', '-' * 50, '\n')

def main(): 
    # Calls function to display the start of project
    projectStart()

    # get Input > call shenanigans() > call monthValidation()
    month, checks, monthIndex = getUserInput()

    # Calc Fees
    totalFees = calculateFees(monthIndex, checks)

    # print summary
    printSummary(month, checks, totalFees)

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()




'''

    
    
    | STATIC - VARIABLES |
    
        (flatFee) is $10/Month
            pre-set @ 10 such that: (flatFee = flatFee * check)
        
        
        MONTH DICTIONARY
            monthsDict = {
                1: ['jan', 'january],
                2: ['feb, 'febuary'],
                ...
            }
    
            Able to:
                1) determine the numerical equivelant for the following: 
                    2) handeled input version the month for which the user provides 
                        e.g.: (jan, jAn, jANUary, 1, 01)

        
    | DEPENDENT - VARIABLES |
    
        BANK FEES
            additionalFees = (dependent on check range logic)
    
    
        MONTH VARS (after handling months input and dictionary coordination)
            month = 'string value' for key in monthsDict (user input version => this version: dictionary key index value)
            monthValue = key number for key in monthsDict
            
            
    | INPUT - VARIABLES |
    
        MONTH (string)
            month = (in any standard format)

        CHECKS
            checks = (in integer format)
                not decimal compatible
                not equal to <0
            
            
    | FUNCTIONS |
    
        def getUserInput()
            get:
                month from shenanigans
                checks from shenanigans
                
                
        def shenanigans(month, checks)
        
            get month from user
                validate datatype
                    pass to monthHandler
                        get month back
            get checks from user
                validate datatype
                    validate not <0 condition
                    
            return month, checks
            
        def monthHandler(month)
            defines & stores:
                monthDict
            
            if month in dict:
                store key as month
                value as monthValue
            else:
                return None

            return month, monthValue
            
            
        def calcFees(months, checks)
        
            calc flatFees (as static solution per requirements)
            
            calc bankFees (as conditional logic solution per requirements)
            
            calc totalFees = flatFees + bankFees
        
        return totalFees

        def displayFees(monthValue, checks, totalFees)
            for vars in variablesList:
                print (vars: to styling specification outline per requirements)

'''