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
    print('\t  Grade Statistics | File embeded data stats')
    print(' ' * 4,'-' * 80)

# Display End of Program Boiler EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print(' ' * 4,'-' * 80)
    print( ' ' * 5, 'End of Project 6')
    print(' ' * 4,'-' * 80)    
    
    
# Read data file then return the list of variables stored
#  ------------------------------------------------------------------------
def readData():

    varList = []

    with open("data.txt", 'r') as file:
        for line in file:
            varList.append(int(line.strip()))


    # --------------------#
    file.close()
    # ^^ DO NOT DELETE ^^
    # --------------------#
    
    return varList
    

def storeVars(varList):
    stats = {
        'list': varList,
        'avg': 0.00,
        'count': 0,
        'sum':0,
        'max': 0,
        'min':0
    }

    statVars, statKeys = [], []

    statVars = processVars(stats)
    
    for keys in stats:
        statKeys.append(keys)
        
    return stats, statVars, statKeys

# Process for variables
#  ------------------------------------------------------------------------
def processVars(stats):

    listSum = sum(stats['list'])
    listCount = len(stats['list'])
    listAvg = f"{(listSum / float(listCount)):.2f}"
    listMax = max(stats['list'])
    listMin = min(stats['list'])

    return listAvg, listCount, listSum, listMax, listMin

def calcVars(stats, statVars, statKeys):

    for count in range(1,len(stats)):
        stats.update({statKeys[count]: statVars[count-1]})

    return stats, statVars, statKeys

# Print Summary
#  ------------------------------------------------------------------------
def displaySummary(varList, stats):
    
    print(f"\t  The numbers are {stats['list'][0],stats['list'][1],stats['list'][2]}")
    print(f"\t  The count of numbers is {stats['count']}")
    print(f"\t  The sum of numbers is {stats['sum']}")
    print(f"\t  The average of the numbers is {stats['avg']}")
    print(f"\t  The max number is {stats['max']}")
    print(f"\t  The min number is {stats['min']}\n")



###############################################################
##    MAIN FUNCTION                                          ##
###############################################################

def main(): 
    # Calls function to display the start of project
    projectStart()

    varList = readData()
    
    stats, statVars, statKeys = storeVars(varList)

    stats, statVars, statKeys = calcVars(stats, statVars, statKeys)
    
    displaySummary(varList, stats)

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main


'''
 NOTES: dashes * 80 for meta data, 76 for program content
__________________________________________________________________

| REQUIREMENTS | 

    - reads a file named data.txt
        is a list of integer values.
            (e.g., student grades)
            
    - read the file
    
    - create a list of the numbers
    
    - Calculate required statistics for summary
    
    - print statistics summary

 
| FILE STANDARDS |

    - File Format (data.txt): 
    - Each line contains a single integer (new line seperation)

| STATIC - VARIABLES |

    - dataLines | integer list of numbers in lines of data.txt
    - lineCount | elements count for dataLines
    - lineVarSum | sum of the numbers in dataLines
    - averageLines | averaged number from dataLines element values
    - maxNum | Maximum value in dataLines
    - minNum | Minimum value in dataLines

| DYNAMIC - VARIABLES |

    - loop vars for conducting operations on the dataLines to store as the other statics    

| DISPLAY |

    REQUIRED:
        Display following for list values:
            - average (rounded to 2 hundreths place as a float)
            - all numbers
            - count
            - sum
            - maximum
            - minimum

    display schema:
        'The numbers are {1,2,3}'
        'The count of numbers is {} '
        'The sum of numbers is {} '
        'The average of the numbers is {var.2f} '
        'The max number is {} '
        'The min number is {} '

| FUNCTIONS |

    REQUIRED
        - readData() | Reads file, returns integer list
        - main() | ORCHESTRATES
        
    def storeVars(): | Store variables
    
    def processVars(): | Processng for vars
    
    def displaySummary(): | Print summary

_______________________________________________________

  OUTPUT PREVIEW
____________________

Project #6 
Written by: Ally Baba 
----------------------------------------------- 
    Grade Statistics Summary 
    -------------------------------------------
    The numbers are 90, 100, 80 
    The count of numbers is 3 
    The sum of numbers is 270 
    The average of the numbers is 90.00 
    The max number is 100 
    The min number is 80 
 
------------------------------------------------
End of Project 6 
 


'''
