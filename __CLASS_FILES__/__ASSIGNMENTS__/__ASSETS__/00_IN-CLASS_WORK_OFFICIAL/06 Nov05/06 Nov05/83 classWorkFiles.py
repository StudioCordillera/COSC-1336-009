# Ally Baba
# November, 2025
# Classwork #780
# ----------------------------
# Project Objectives
#   Learning Files
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tLearning Files")
    print("-" * 60)

# This fucntion will display the end of project
def projectEnd():
    print('\n')
    print('-' * 60)
    print('\tEnd of project')

# This function will get the user's entry for a float
def getFloatData(prompt):
    while (True):
        try:
            
            value = float(input(prompt))

            return value

        except ValueError:
            print('\t\tERRor MSG! Non numbers entered')

# This fucntion will get the user's entry for an integer
def getIntegerData(prompt):

    while (True):
        try:
            value = int(input(prompt))

            if (value >= 1 and value <= 5):
                return value
            else:
                print('\t\tError MSG! Enter values between 1 and 5')

        except ValueError:
            print('\t\tERRor MSG! Non numbers entered')

# This function will get the user's entry of string
def getStringData(prompt):
    value = input(prompt).strip(' ')

    return value

# This function will get a char input
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()

        if (value in ['B', 'C', 'X']):
            return value
        else:
             print('\t\tERRor MSG! Enter B | C | X')

def main():
    # Display start of project
    projectStart()

    # object (variable names that assigns the file)
    try:
        fileRead = open('data.txt', 'r')

        for line in fileRead:
            line = line.strip('\n').strip(' ')

            print(line)
        
        fileRead.close()

    except FileNotFoundError:
        print('\t\tERRor MSG! File is here')
    
    # Display end of project
    projectEnd()
   
main()

# Trace:








