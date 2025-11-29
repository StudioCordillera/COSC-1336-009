
# This function will return an integer input from the user
def getIntegerData(prompt):
    value = int(input(prompt))
    return value

# This function will return a float input from the user
def getFloatData(prompt):
    value = float(input(prompt))
    return value

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

'''
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

inFuncs = {
    int: getIntegerData,
    str: getStringData,
    float: getFloatData
}

inVars = {
        
    
    
}

month = month.upper()

for keys in monthList:
    inVars[type(month)] = 

        # print(inVars[inVars.index(month)])
        # sprint(inFuncs[inFuncs.index(inVars[inVars.index(month)])])
        #print(month, ' Is @: ', monthList[keys].index(month), 'in key: ', keys)
        

'''

'''

        
monthList = {
    1: {
        'abbr':{'JAN'},
        'full':'JANUARY'
    },
    2: {
        'abbr':{'FEB'},
        'full':'FEBUARY'
    },
    3: {
        'abbr':{'MAR'},
        'full':'MARCH'
    },
    4: {
        'abbr':{'APR'},
        'full':'APRIL'
    },
    5: {
        'abbr':{'MAY'},
        'full':'MAY'
    },
    6: {
        'abbr':{'JU7'},
        'full':'JUNE'
    },
    7: {
        'abbr':{'JUL'},
        'full':'JULY'
    },
    8: {
        'abbr':{'AUG'},
        'full':'AUGUST'
    },
    9: {
        'abbr':{'SEP', 'SEPT'},
        'full':'SEPTEMBER',
    },
    10: {
        'abbr':{'OCT'},
        'full':'OCTOBER'
    },
    11: {
        'abbr':{'NOV'},
        'full':'NOVEMBER'
    },
    12: {
        'abbr':{'DEC'},
        'full':'DECEMBER'
    }
}

print(monthList.items())

for keys, objects in monthList:
    print(keys)
    



inFuncs = {
    1: ['checks', getIntegerData, '\tEnter the month: '],
    2: ['month', getStringData, '\tEnter the month: ']
}

print(inFuncs[1][0])

for x in inFuncs[1]:
    print(x)
    
'''
month = 'eight'
month = int(month) + 1
print (month)