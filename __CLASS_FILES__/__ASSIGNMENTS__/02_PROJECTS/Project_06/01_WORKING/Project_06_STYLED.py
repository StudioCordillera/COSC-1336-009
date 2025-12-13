###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   November 26, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################

# CLI Styling Constants (Subtle Enhancement)
# ─────────────────────────────────────────────────────────────
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

# Colors (Subtle, Professional)
CYAN = '\033[36m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'

# Box Drawing
BOX_H = '─'
BOX_V = '│'
BOX_TL = '┌'
BOX_TR = '┐'
BOX_BL = '└'
BOX_BR = '┘'
BOX_HEAVY_H = '━'
BOX_DOUBLE_H = '═'
BOX_DOUBLE_V = '║'
BOX_DOUBLE_TL = '╔'
BOX_DOUBLE_TR = '╗'
BOX_DOUBLE_BL = '╚'
BOX_DOUBLE_BR = '╝'

# Symbols
CHECK = '✓'
ARROW_RIGHT = '▶'
BULLET = '•'
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

#   SOPB - Styled Banner
#  ------------------------------------------------------------------------
def projectStart():
    # Main title box with double lines
    print(f"\n{CYAN}{BOLD}{'═' * 80}{RESET}")
    print(f"{CYAN}{BOLD}║{' ' * 24}PROJECT 06 - STATISTICS{' ' * 32}║{RESET}")
    print(f"{CYAN}║{' ' * 20}Grade Statistics from File Data{' ' * 28}║{RESET}")
    print(f"{CYAN}{BOLD}{'═' * 80}{RESET}")
    
    # Author info box with standard ASCII
    print(f"{DIM}    .{'─' * 71}.{RESET}")
    print(f"{DIM}    | {ARROW_RIGHT} Written by: {BOLD}Matthew Ochoa{RESET}{DIM}{' ' * 42}|{RESET}")
    print(f"{DIM}    | {ARROW_RIGHT} Date: {BOLD}November 26, 2025{RESET}{DIM}{' ' * 44}|{RESET}")
    print(f"{DIM}    | {ARROW_RIGHT} Class: {BOLD}COSC 1336{RESET}{DIM}{' ' * 51}|{RESET}")
    print(f"{DIM}    '{'─' * 71}'{RESET}\n")

#   EOPB - Styled Banner
#  ------------------------------------------------------------------------
def projectEnd():
    print(f"\n{GREEN}{BOLD}    {'━' * 72}{RESET}")
    print(f"{GREEN}{BOLD}    {CHECK} PROGRAM COMPLETED SUCCESSFULLY{RESET}")
    print(f"{GREEN}{BOLD}    {'━' * 72}{RESET}\n")    
    
    
#   Get File Data
#  ------------------------------------------------------------------------
def readData():

    varList = [] # INIT
    with open("data.txt", 'r') as file:         # OPEN <
        for line in file:                       # EXTRACT <
            varList.append(int(line.strip()))   # COLLECT >

    # --------------------#
    file.close()                                # CLOSE ><
    # ^^ DO NOT DELETE ^^
    # --------------------#
    
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

#   Variable Summary - Styled Output
#  ------------------------------------------------------------------------
def displaySummary(varList, stats):
    # Header box with enhanced styling
    print(f"\n{BOLD}{CYAN}    {'═' * 72}{RESET}")
    print(f"{BOLD}{CYAN}    ║{' ' * 22}STATISTICAL SUMMARY{' ' * 28}║{RESET}")
    print(f"{CYAN}    {'═' * 72}{RESET}\n")
    
    # Data section with visual grouping
    print(f"{BOLD}{CYAN}    [{' INPUT DATA '}]{RESET}")
    print(f"{BOLD}{' ' * 6}{BULLET} Data Set:{RESET} {YELLOW}{stats['list'][0]}, {stats['list'][1]}, {stats['list'][2]}{RESET}")
    print(f"{DIM}{' ' * 6}{'─' * 64}{RESET}\n")
    
    # Statistics section with icons and better spacing
    print(f"{BOLD}{CYAN}    [{' COMPUTED STATISTICS '}]{RESET}")
    print(f"{BOLD}{' ' * 6}{BULLET} Count:{RESET}{' ' * 7}{BLUE}│{RESET} {BLUE}{stats['count']}{RESET} values")
    print(f"{BOLD}{' ' * 6}{BULLET} Sum:{RESET}{' ' * 9}{BLUE}│{RESET} {BLUE}{stats['sum']}{RESET}")
    print(f"{BOLD}{' ' * 6}{BULLET} Average:{RESET}{' ' * 5}{GREEN}│{RESET} {GREEN}{BOLD}{stats['avg']}{RESET}")
    print(f"{BOLD}{' ' * 6}{BULLET} Maximum:{RESET}{' ' * 5}{MAGENTA}│{RESET} {MAGENTA}{stats['max']}{RESET}")
    print(f"{BOLD}{' ' * 6}{BULLET} Minimum:{RESET}{' ' * 5}{MAGENTA}│{RESET} {MAGENTA}{stats['min']}{RESET}")
    
    print(f"\n{DIM}    {'─' * 72}{RESET}\n")

###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 

    # SOPB
    projectStart()

    #| 1. Extract | 2. Store | 3. Process | 4. Print |
    print(f"{CYAN}    [{'─' * 8}]{RESET} {DIM}PIPELINE EXECUTION{RESET} {CYAN}[{'─' * 8}]{RESET}\n")
    
    print(f"{DIM}{' ' * 4}[1/3] {ARROW_RIGHT} Reading data from file...{RESET}")
    varList = readData()
    print(f"{GREEN}{' ' * 4}      {CHECK} Data loaded successfully{RESET} {DIM}({len(varList)} values){RESET}\n")
    
    print(f"{DIM}{' ' * 4}[2/3] {ARROW_RIGHT} Processing statistics...{RESET}")
    stats, statVars, statKeys = processVars1(varList)
    stats, statVars, statKeys = calcVars(stats, statVars, statKeys)
    print(f"{GREEN}{' ' * 4}      {CHECK} Calculations complete{RESET} {DIM}(6 metrics computed){RESET}\n")
    
    print(f"{DIM}{' ' * 4}[3/3] {ARROW_RIGHT} Generating report...{RESET}")
    
    displaySummary(varList, stats)

    # EOPB
    projectEnd()

main() #<= | Call Main