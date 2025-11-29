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

    print(stats.items())
    
    statVars = processVars(stats)

    print(len(stats))
    print(statKeys)
    
    for keys in stats:
        statKeys.append(keys)
        
    print(len(stats))
    print(statKeys)

    return stats, statVars, statKeys

def processVars(stats):
    
    listSum = sum(stats['list'])
    listCount = len(stats['list'])
    listAvg = f"{(listSum / float(listCount)):.2f}"
    listMax = max(stats['list'])
    listMin = min(stats['list'])
    
    return listAvg, listCount, listSum, listMax, listMin

def calcVars(stats, statVars, statKeys):

    for count in range(1,len(stats)):
        print (count)
        stats.update({statKeys[count]: statVars[count-1]})

    return stats, statVars, statKeys


# Print Summary
#  ------------------------------------------------------------------------
def displaySummary(varList, stats):
    
    print(varList)
    for items in varList:
        print(items)

    print(stats)
    for keys in stats:
        print(keys)

    return 



def main():
    
    varList = readData()
    
    stats, statVars, statKeys = storeVars(varList)

    stats, statVars, statKeys = calcVars(stats, statVars, statKeys)
        
        
    print(stats.items())

        
        
    
    
main()




    
'''

def processVars(stats):
    
    listSum = sum(stats['list'])
    listCount = len(stats['list'])
    listAvg = f"{(listSum / float(listCount)):.2f}"
    listMax = max(stats['list'])
    listMin = min(stats['list'])
    
    return listAvg, listCount, listSum, listMax, listMin
    
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
    
for count in range(1,len(stats)):
    print (count)
    stats.update({statKeys[count]: statVars[count-1]})

'''

          
          