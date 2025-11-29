
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

def vars():

    # init vars
    monthlyRent = 2500
    Tenant, month = '', ''
    day, year, daysLate, lateFees = 0, 0, 0, 0
    usageFee, totalDue = 0.0, 0.0
    
    varKeys = {
        

            'Tenant': {
                'prompt' : '\tEnter Tenant name: ',
                'variable': Tenant
            },
            
            'Month': {
                'prompt' : '\tEnter payment month: ',
                'variable': month
            },

            'Day':{
                'prompt' : '\tEnter payment day: ',
                'variable' : day,
            },

            'Year':{
                'prompt' : '\tEnter payment year: ',
                'variable': year
            },

            'Usage Fee': {
                'prompt' : '\tEnter usage fee: ',
                'variable' : usageFee
            }
        }
        
    return varKeys

def shenanigans(dataType, prompt, inFunc):
    # Call the appropriate input function and return the value
    returnValue = inFunc[dataType](prompt)
    return returnValue
 
    # while True:
    #     if value is str:
    #             variable = getStringData(prompt).strip().lower()
    #             
    #             if listNeeded is not None:
    #                 if variable not in listNeeded:
    #                     print('\t\tENTER A MONTH!!')
    #                 else:
    #                     break
    #             else:
    #                 break
    # 
    #     elif dataType is int:
    #         try:
    #             variable = getIntegerData(prompt)
    #             if (variable > 0):
    #                 break
    #             else:
    #                 print('\t\tONLY POSITIVE + NON-ZERO NUMBERS!!')
    #         except ValueError:
    #             print('\t\tONLY INTEGER DATA!!')
    # 
    #     elif dataType is float:
    #         try:
    #             variable = getFloatData(prompt)
    #             if (variable > 0):
    #                 break
    #             else:
    #                 print('\t\tONLY POSITIVE + NON-ZERO NUMBERS!!')
    #         except ValueError:
    #             print('\t\tONLY NUMERICAL DATA!!')
                

# ___________________________________________________________________

def main():
    
    monthList = {
        'january': 1, 'jan': 1,
        'february': 2, 'feb': 2, 
        'march': 3, 'mar': 3, 
        'april': 4, 'apr': 4, 
        'may': 5, 
        'june': 6, 'jun': 6,
        'july': 7, 'jul': 7,
        'august': 8, 'aug': 8,
        'september': 9, 'sep': 9, 'sept': 9,
        'october': 10, 'oct': 10,
        'november': 11, 'nov': 11,
        'december': 12, 'dec': 12,
        }
    
    inFunc = {
        int : getIntegerData,
        str : getStringData,
        float : getFloatData,
    }
    
    varKeys = vars()
    
    # print(varKeys.items())
    # print(varKeys['Tenant']['variable'])
    # print(varKeys['Tenant']['prompt'])
    
    for key in varKeys:
        # Get the current variable's type and prompt
        varType = type(varKeys[key]['variable'])
        prompt = varKeys[key]['prompt']
        
        # Get user input using the appropriate function
        userInput = shenanigans(varType, prompt, inFunc)
        
        # Store the result back in the dictionary
        varKeys[key]['variable'] = userInput
        
        print(f"{key}: {userInput}")
        
        
    #    while True:
    #        try:
    #            varKeys[key]['variable'] = shenanigans(type(varKeys[key]['variable']), varKeys[key]['prompt'], inFunc))

    #            if (varKeys[key] == 'Month'):
    #                if (varKeys[key]['variable'] not in monthList):
    #                    print('\t\tONLY MONTHS IN FULL OR ABBREVIATED NOTATION!!')                        
    #            else:
    #                break   

    #        except ValueError:
    #            value = varKeys[key]['variable']
    #            print(f'\t\tONLY {type(value)} TYPE VARIABLES!!')
    
    
main()