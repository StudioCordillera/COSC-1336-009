########################################
## Matthew Ochoa                   #####
## MONTH ##, #yr#                  #####
## Project: ##                     #####
## Status: In - Progress           #####
## Class: COSC 1336                #####
########################################
import os
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

#  Clear Console Utility
#  ------------------------------------------------------------------------
def clearTerminal():
    os.system('cls')


def checkFile(name):
    """Check if file exists in current directory or subdirectories"""
    current_dir = os.getcwd()
    
    # Walk through directory tree
    for dirpath, dirnames, filenames in os.walk(current_dir):
        if name in filenames:
            full_path = os.path.join(dirpath, name)
            return True, name, full_path
    
    # If we get here, file wasn't found
    return False, None, None




#  read data
#  ------------------------------------------------------------------------
def readData():
    pass

'''    - readData() 
        - Opens file
        - reads file. 
        - Parses file lines
            - populates dictionary from lines
        - Returns the dictionary
'''

def writeData():
    
    for key, content in data_dict.items():
        filename = f"{key}{extension}"
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'w') as file:
            file.write(str(content))
    
    print(f"Wrote {len(data_dict)} files to {directory}")

#  Display Results
#  ------------------------------------------------------------------------
def displayResults(studentID, studentName):
    pass

'''
    - displayResult(studentID, studentName) 
        - takes student ID
        - takes name (or error message)
        - displays the result. 



def mainMenu():
    """Display formatted mainMenu"""
    mainMenu = """
╔════════════════════════════════╗
║        STUDENT SYSTEM          ║
╠════════════════════════════════╣
║  1. Add Student                ║
║  2. Search Student             ║
║  3. Display All                ║
║  4. Exit                       ║
╚════════════════════════════════╝
"""
    return get_menu_choice(mainMenu)

def get_menu_choice(mainMenu):
    """Get and validate mainMenu choice"""
    while True:
        clearTerminal()
        print(mainMenu)
        choice = input("Enter choice: ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        clearTerminal()
        print("Invalid choice. Try again.")
        input()
        clearTerminal()
'''


    
'''
def read_files_to_dict(directory, extension='.txt'):
    """Read all files with extension into dictionary"""
    if not os.path.isdir(directory):
        return {}
    
    files_dict = {}
    
    
    
def saveState(self, config_dict, config_path="config.txt"):
    """Write dictionary to config file"""
    directory = os.path.dirname(config_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(config_path, 'w') as file:
        for key, value in config_dict.items():
            file.write(f"{key}={value}\n")
    
    

# Pattern 3: Write dictionary entries to separate files
def write_dict_to_files(data_dict, directory, extension='.txt'):
    """Write each dictionary entry to separate file"""
    os.makedirs(directory, exist_ok=True)
    
    for key, content in data_dict.items():
        filename = f"{key}{extension}"
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'w') as file:
            file.write(str(content))
    
    print(f"Wrote {len(data_dict)} files to {directory}")

'''
            

###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 
    # Calls function to display the start of project
    projectStart()

    getLastState()

    choice = mainMenu()

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()


''' ┌─── CLASS ───────────────────────────────────┐
    │                                             |
    |    STATE                                    │
    │        - provides object for ease of use    │
    │                                             │
    └─────────────────────────────────────────────┘
'''
class State:
    def __init__(self):
        # Initialize attributes first with default values
        self.students = []
        self.dPath = None
        self.dName = None
        self.stateP = None
        self.stateN = None
        
        # Now we can use them in dictionaries
        self.dataFile = {
            'path': self.dPath,
            'name': self.dName
        }
        self.stateFile = {
            'path': self.stateP,
            'name': self.stateN
        }
        
        self.studentList = {}

        self.state = {
            'dataFile': self.dataFile,
            'stateFile': self.stateFile,
            'studentList': self.studentList
        }

    def saveStudent(self):
        pass
    def removeStudent(self):
        pass
    def registerStudent(self):
        pass
    def loadStudent(self):
        pass

    def initState(self):
        """Initialize state by checking/creating necessary files"""
        
        # Check for data file
        dFileCheck, DName, DPath = checkFile('data file.txt')
        
        if dFileCheck:
            self.dPath = DPath
            self.dName = DName
            self.dataFile['path'] = DPath
            self.dataFile['name'] = DName
        else:
            # Create data file if it doesn't exist
            filepath = './data file.txt'
            with open(filepath, 'w') as file:
                file.write('')
            self.dPath = os.path.abspath(filepath)
            self.dName = 'data file.txt'
            self.dataFile['path'] = self.dPath
            self.dataFile['name'] = self.dName
            print(f"Created {self.dName} file in {os.getcwd()}")

        # Check for state file
        sFileCheck, stateN, stateP = checkFile('state.txt')
        
        if sFileCheck:
            self.stateP = stateP
            self.stateN = stateN
            self.stateFile['path'] = stateP
            self.stateFile['name'] = stateN
        else:
            # Create state file if it doesn't exist
            filepath = './state.txt'
            with open(filepath, 'w') as file:
                file.write('')
            self.stateP = os.path.abspath(filepath)
            self.stateN = 'state.txt'
            self.stateFile['path'] = self.stateP
            self.stateFile['name'] = self.stateN
            print(f"Created {self.stateN} file in {os.getcwd()}")


    def loadState(self, state, stateFile):
        with open(stateFile['path'], 'r') as file:
            name = os.path.splitext('state')[0]
            state[name] = file.read()

        return state
    
    def saveState(self, state, stateFile):

        config_path = stateFile['path']
        
        directory = os.path.dirname(config_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(config_path, 'w') as file:
            for key, value in state.items():
                file.write(f"{key}={value}\n")

        
    def set_dataFile(self, dataFile):
        self.dataFile = dataFile
    def set_dPath(self, dPath):
        self.dPath = dPath
    def set_dName(self, dName):
        self.dName = dName
    def set_stateP(self, stateP):
        self.stateP = stateP
    def set_stateN(self, stateN):
        self.stateN = stateN
    def get_stateN(self):
        return self.stateN
    def get_stateP(self):
        return self.stateP
    def get_dName(self):
        return self.dName
    def get_dPath(self):
        return self.dPath
    def get_dataFile(self):
        return self.dataFile
    


class Student:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        














'''

| REQUIREMENTS | 

| FILE STANDARDS |

| STATIC - VARIABLES |

| DYNAMIC - VARIABLES |

| INPUT - VARIABLES |

| DERIVED - VARIABLES |

| DISPLAY |

| FUNCTIONS |


creates
    - initializes db
    - students in db
manages
    - db entries
    - db student items

dictionary
    - ID | key 
    - name | value


Functional Requirements 
    1. Data Input: 
        The program will read from a text file (e.g., data.txt) that contains student records. 
        Each line in the file will be in the format: 
            studentID,studentName 

    2. Dictionary Creation 
        - The program will parse the file and populate a dictionary where: 
            - studentID → dictionary key 
            - studentName → dictionary value 

    3. User Interaction 
        - Continously prompts for student ID
            - ID found | display student name for ID
            - ID not found | display: "Student Not Found"
        - input 'N' | (not case-sensitive) to stop. 

Required Functions 
    - getStringData() 
        - Get input provided prompt 
        - non-empty input validation
        - 'Y' or 'N' | exit prompts uppercase

    - readData() 
        - Opens file
        - reads file. 
        - Parses file lines
            - populates dictionary from lines
        - Returns the dictionary

    - displayResult(studentID, studentName) 
        - takes student ID
        - takes name (or error message)
        - displays the result. 


Additional Guidelines 
• Validate user input (no empty strings). 
• Follow professional programming practices (naming conventions, indentation, 
documentation). 
• Include comments at the beginning of the file and before each function.  


_______________________________________________________

  OUTPUT PREVIEW
____________________

Project #8 
Written by: Ally Baba 
----------------------------------------------- 
    Search Student Information 
    -------------------------------------------------------------------------------- 
        Are you ready to search? (Y/N) Y 
        Please enter a student ID: A007 
    
    -------------------------------------------------------------------------------- 
    Query Summary: Student Information  
    -------------------------------------------------------------------------------- 
        Student Found 
        Name: Ally Baba 
        ID: A007 

        Are you ready to search? (Y/N) Y 
        Please enter a student ID: X007 
    
    -------------------------------------------------------------------------------- 
    Query Summary: Student Information  
    -------------------------------------------------------------------------------- 
        Student Not Found 
        Are you ready to search? (Y/N) N 
        You have searched 2 times 
 
-------------------------------------------------------------------------------- 
End of Project 8 
 

'''