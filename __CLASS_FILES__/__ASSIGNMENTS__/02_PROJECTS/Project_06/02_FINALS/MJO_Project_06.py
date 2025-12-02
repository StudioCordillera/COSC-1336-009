###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   November 26, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   REQUIREMENTS                                              |
|_____________________________________________________________|
|                                                             |
|  - reads                                                    |
|        - data.txt | (integer value list)                    |
|    - Lines contain single integer ( seperation by >\n< )    | 
|    - stores data in lines                                   |
|        - in list                                            |
|    - Calculate                                              |
|        - statistics                                         |
|    - print stats with summary                               |
|_____________________________________________________________|
|                                                             |
|   DISPLAY                                                   |
|_____________________________________________________________|
|                                                             |
|    REQUIRED:                                                |
|        Display following for list values:                   |
|            - average (place val = 0.00)                     |
|            - all numbers                                    |
|            - count                                          |
|            - sum                                            |
|            - maximum                                        |
|            - minimum                                        |
|_____________________________________________________________|
|                                                             |
|   FUNCTIONS                                                 |
|_____________________________________________________________|
|                                                             |
|    REQUIRED                                                 |
|        - readData()           | Extract Var < data.txt      |
|        - main()               | ORCHESTRATES                |
|                                                             |
|    OPTIONAL                                                 |
|        - storeVars():         | Store variables             |
|        - storeVars():         | Processng for vars          |
|        - displaySummary():    | Print summary               |
|                                                             |
|_____________________________________________________________|
|                                                             |
|   STATIC VARIABLES                                          |
|_____________________________________________________________|
|                      |                                      |
|      - dataLines     |   integer list FROM data.txt         |
|      - lineCount     |   elements count for dataLines       |
|      - lineVarSum    |   sum of the numbers in dataLines    |
|      - averageLines  |   avg values in dataLines            |
|      - maxNum        |   Maximum value in dataLines         |
|      - minNum        |   Minimum value in dataLines         |
|                                                             |
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
    print(' ' * 4, '-'* 80, '\n',' ' * 4, 'Start of Project 4')
    print(' ' * 5, 'Written by: Matthew Ochoa')
    print(' ' * 5,'Date: 11/25/2025 ')
    print(' ' * 4,'-' * 80)
    print('\t  Grade Statistics | File embeded data stats')
    print(' ' * 4,'-' * 80)

#   EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print(' ' * 4,'-' * 80)
    print( ' ' * 5, 'End of Project 6')
    print(' ' * 4,'-' * 80)    
    
    
#   Get File Data
#  ------------------------------------------------------------------------
def readData():

    varList = [] # INIT
    with open("data.txt", 'r') as file:         # OPEN <
        for line in file:                       # EXTRACT <
            varList.append(int(line.strip()))   # COLLECT >
    
    return varList                              # SEND TO MAIN >

#   Variables Pipeline
#  ------------------------------------------------------------------------   
def processVars1(varList):
    stats = {
        'list': varList,
        'avg': 0.00,
        'count': 0,
        'sum':0,
        'max': 0,
        'min':0
    }
    statVars, statKeys = [], []     # INIT
    statVars = processVars(stats)   # Catch processed vars <
    for keys in stats:              # From Keys < Get Values > 
        statKeys.append(keys)       # > iterate into List

    return stats, statVars, statKeys # Ship Var lists to main >

#   Variable Processing 
#  ------------------------------------------------------------------------

def processVars(stats): # From Data Extract + Stat Placehoders <

    listSum = sum(stats['list'])                    # |
    listCount = len(stats['list'])                  # |
    listAvg = f"{(listSum / float(listCount)):.2f}" # | < Find Dependent
    listMax = max(stats['list'])                    # |    Stat Vars
    listMin = min(stats['list'])                    # |

    return listAvg, listCount, listSum, listMax, listMin # Send stats

def calcVars(stats, statVars, statKeys):

    for count in range(1,len(stats)):
        stats.update({statKeys[count]: statVars[count-1]})

    return stats, statVars, statKeys

#   Variable Summary
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

    # SOPB
    projectStart()

    #| 1. Extract | 2. Store | 3. Process | 4. Print |
    varList = readData()
    stats, statVars, statKeys = processVars1(varList)
    stats, statVars, statKeys = calcVars(stats, statVars, statKeys)
    displaySummary(varList, stats)

    # EOPB
    projectEnd()

main() #<= | Call Main