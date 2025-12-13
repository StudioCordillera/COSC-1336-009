# MATTHEW OCHOA CODING STANDARDS - HARDLINE REQUIREMENTS
## Based on Comprehensive Analysis of Project_09

**Date Created:** December 12, 2025  
**Reference Project:** Project_09 (VROOM - Drive a Chosen Car!)  
**Status:** ABSOLUTE STANDARD - NO DEVIATIONS ALLOWED

---

## 📋 TABLE OF CONTENTS

1. [File Structure Requirements](#file-structure-requirements)
2. [Header Format](#header-format)
3. [Import Patterns](#import-patterns)
4. [Context Setup](#context-setup)
5. [Variable Naming Conventions](#variable-naming-conventions)
6. [Class Architecture](#class-architecture)
7. [Print Statement Requirements](#print-statement-requirements)
8. [Formatting Constants Usage](#formatting-constants-usage)
9. [Validation Patterns](#validation-patterns)
10. [Menu System Patterns](#menu-system-patterns)
11. [File Reading Patterns](#file-reading-patterns)
12. [Loop Validation Patterns](#loop-validation-patterns)
13. [Function/Method Naming](#functionmethod-naming)
14. [Documentation Standards](#documentation-standards)
15. [Forbidden Practices](#forbidden-practices)

---

## 1. FILE STRUCTURE REQUIREMENTS

### Main Project File Structure:
```
ProjectName/
├── 00_IMPORT/
│   └── requirements.txt (optional)
├── 01_WORKING/
│   ├── ProjectName_WORKING.py
│   ├── data.txt (if needed)
│   ├── MyClasses/
│   │   ├── displayLabels.py
│   │   └── typeValidation.py
│   └── ProjectClasses/
│       └── specificClass.py
└── 02_FINALS/
    ├── MJO_ProjectName.py
    ├── data.txt (if needed)
    ├── MyClasses/
    │   ├── displayLabels.py
    │   └── typeValidation.py
    └── ProjectClasses/
        └── specificClass.py
```

**RULES:**
- MyClasses folder ALWAYS contains: `displayLabels.py`, `typeValidation.py`
- ProjectClasses folder contains project-specific classes
- Data files (data.txt) in same directory as main file
- 01_WORKING for development, 02_FINALS for completed code
- Finals use MJO_ prefix naming convention

---

## 2. HEADER FORMAT

**EXACT FORMAT - NO VARIATIONS:**

```python
###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 10, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
```

**RULES:**
- Always use `###` borders (60 hashes for top/bottom lines)
- Always use `##:::::` prefix pattern
- Spaces must align EXACTLY as shown
- Date format: `Month DD, YYYY` (e.g., `December 10, 2025`)
- Status field: `COMPLETE`, `IN PROGRESS`, or `TESTING`
- Class field: `COSC 1336` (or current class)

---

## 3. IMPORT PATTERNS

### Main File Import Pattern:
```python
from MyClasses import displayLabels
from ProjectClasses import vehiclesClass

Project9=displayLabels.Context(9, '12/08/2025','VROOM', 'Drive a Chosen Car!')
END, START = Project9.END, Project9.START
Car=vehiclesClass.Car
```

**RULES:**
- Import modules, NOT individual functions/classes (use `from MyClasses import displayLabels`)
- Context object uses CapitalCase matching project name/number
- Extract START and END immediately: `END, START = Project9.END, Project9.START`
- Create class shortcuts AFTER Context setup: `Car=vehiclesClass.Car`
- NO wildcard imports (`from module import *`)

### Class File Import Pattern:
```python
import sys
import os
# Add parent directory to path if running from ProjectClasses folder
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from MyClasses import displayLabels, typeValidation
nL, tab, tab1, lineGraph, shortBar, medBar = displayLabels.nL, displayLabels.tab, displayLabels.tab1, displayLabels.lineGraph, displayLabels.shortBar, displayLabels.medBar
Project9=displayLabels.Context(9, '12/08/2025','VROOM', 'Drive a Chosen Car!')
START=Project9.START
v=V=typeValidation.validateInput
```

**RULES:**
- ALWAYS include sys/os path manipulation for standalone testing
- Import formatting constants explicitly: `nL, tab, tab1, lineGraph, shortBar, medBar = displayLabels.nL, ...`
- Create validation shorthand: `v=V=typeValidation.validateInput`
- Context setup duplicated in class files for independence
- Extract only START if END not needed

---

## 4. CONTEXT SETUP

### Context Object Creation:
```python
Project9=displayLabels.Context(9, '12/08/2025','VROOM', 'Drive a Chosen Car!')
```

**Parameters (in order):**
1. `projectNum` (int): Project number (e.g., `9`)
2. `finalDate` (str): Due date in format `'MM/DD/YYYY'` (e.g., `'12/08/2025'`)
3. `projectName` (str): Short project title (e.g., `'VROOM'`)
4. `purpose` (str): Project description (e.g., `'Drive a Chosen Car!'`)

**RULES:**
- Variable name matches project: `Project9`, `ExamTwo`, `Project10`
- Date ALWAYS in single quotes with MM/DD/YYYY format
- Project name SHORT and descriptive (1-2 words)
- Purpose describes what user will DO

---

## 5. VARIABLE NAMING CONVENTIONS

### Naming Standards from Project_09:

**Class Names:**
- PascalCase: `Car`, `CarMenu`, `BankAccount`
- Descriptive and specific: NOT `Vehicle`, but `Car`

**Instance Variables:**
- Lowercase with descriptive names: `year`, `make`, `speed`
- NOT abbreviated unless standard: `nL` (newline), `v` (validator)

**Function Parameters:**
- lowercase with type hints: `year:int`, `make:str`, `speed:int`
- Default values for constructors: `year:int = 1000, make:str = 'make', speed:int = 0`

**Local Variables:**
- camelCase or lowercase: `carMakeYear`, `accelerated`, `braked`
- Descriptive names: NOT `x`, `temp`, `data` - use `accelerated`, `braked`, `speed`

**Shortcuts:**
- Validation shorthand: `v=V=typeValidation.validateInput`
- Class shortcuts: `Car=vehiclesClass.Car`
- Format constants: `nL, tab, tab1, lineGraph, shortBar, medBar`

---

## 6. CLASS ARCHITECTURE

### Primary Class Structure (from vehiclesClass.py):

```python
class Car:

    def __init__(self, year:int = 1000, make:str = 'make', speed:int = 0):

        self.year = year
        self.make = make
        self.speed = speed

        GetCar=CarMenu()
        self.car=GetCar.Start()
        self.Constructor(self.car)
        self.Driving(self.make, self.year, self.speed)


    def Constructor(self, car):
        self.year= car[0]
        self.make= f"{car[1]}, {car[2]}"
        return self.year, self.make
    
        
    def printCarInfo(self, make, year):
        os.system('cls')
        START()
        print(f"{tab+tab}My Car Information{nL+tab+tab+medBar}")
        print(f"{tab+tab}Car Make: {make}")
        print(f"{tab+tab}Car Year: {year}")


    def Driving(self, year, make, speed):
        # Main logic here
        pass
```

**ARCHITECTURE RULES:**

1. **`__init__` Orchestrates Everything:**
   - Initialize instance variables first
   - Call helper classes (Menu systems)
   - Call Constructor to set up data
   - Call main logic method (e.g., `Driving()`)
   - `__init__` drives the ENTIRE program flow

2. **Constructor Method Pattern:**
   - Separate `Constructor()` method to process initialization data
   - Takes structured data (list/dict) and assigns to instance variables
   - Returns tuple of key values

3. **Method Naming:**
   - PascalCase for major methods: `Constructor()`, `Start()`, `Driving()`
   - camelCase for utility methods: `printCarInfo()`, `displayMenu()`

4. **Method Organization:**
   - Major flow methods at top
   - Utility/display methods in middle
   - Simple getter/setter at bottom

---

### Secondary Class Structure (Menu/Helper Classes):

```python
class CarMenu():

    def __init__(self):
        self.carMakeYear:list
        self.choices:list
        self.choice:int


    def set_carMakeYear(self, carMakeYear):
        self.carMakeYear = carMakeYear
    def get_carMakeYear(self):
        return self.carMakeYear
    
    def set_choices(self, choices):
        self.choices = choices
    def get_choices(self):
        return self.choices
    def set_choice(self, choice):
        self.choice = choice
    def get_choice(self):
        return self.choice


    def Start(self):
        # Load data
        # Process data
        return self.Provide()
        
    def Provide(self):
        # Display menu
        # Get user choice
        # Validate
        # Return selection
        pass
```

**HELPER CLASS RULES:**
1. Empty `__init__` with type-hinted instance variables
2. Getter/setter methods for ALL instance variables
3. `Start()` method initializes and returns data
4. `Provide()` method handles user interaction
5. Menu classes DON'T print banners - main class does that

---

## 7. PRINT STATEMENT REQUIREMENTS

### ❌ FORBIDDEN - Multiple Separate Print Statements:
```python
# NEVER DO THIS
print(f"{tab}My Car Information")
print(f"{tab}{medBar}")
print(f"{tab}Car Make: {make}")
print(f"{tab}Car Year: {year}")
```

### ✅ REQUIRED - Concatenated Print Statements:
```python
# ALWAYS DO THIS
print(f"{tab+tab}My Car Information{nL+tab+tab+medBar}")
print(f"{tab+tab}Car Make: {make}")
print(f"{tab+tab}Car Year: {year}")
```

**CONSOLIDATION RULES:**

1. **Single Logical Block = Single Print:**
   ```python
   # Title + separator in ONE print
   print(f"{tab+tab}My Car Information{nL+tab+tab+medBar}")
   ```

2. **Use `nL` for Newlines Within f-strings:**
   ```python
   print(f"{tab+dashGraph+nL+tab}BILLING SUMMARY{nL+tab+dashGraph+nL}")
   ```

3. **Concatenate Constants with `+`:**
   ```python
   print(f"{tab+tab1}Accelerate #{count+1}:{tab}Increase by 5 mph{tab}Current speed: {speed}mpg")
   ```

4. **Multi-line Display Example:**
   ```python
   print(f"{tab+tab+lineGraph+nL+nL+tab+tab1}Car Travel Information{nL+tab+tab+lineGraph}")
   print(f"{tab+tab}Acceleration applied:{nL+tab+tab+shortBar}")
   ```

**PATTERN:**
- Related information in SAME print statement
- Use `nL` to add breaks WITHIN the f-string
- Use `+` to concatenate formatting constants
- Minimize total number of print() calls

---

## 8. FORMATTING CONSTANTS USAGE

### Available Constants (from displayLabels.py):
```python
nL = '\n'              # NewLine
tab = '    '           # 4 spaces
tab1 = '     '         # 5 spaces (tab + 1)
longBar = '-'*80       # 80 dashes
medBar = '-'*50        # 50 dashes
shortBar = '-'*12      # 12 dashes
dashGraph = '-'*60     # 60 dashes
lineGraph = '_'*60     # 60 underscores
```

### Usage Patterns from Project_09:

**Title with Separator:**
```python
print(f"{tab+tab}My Car Information{nL+tab+tab+medBar}")
```

**Section Header:**
```python
print(f"{tab+tab+lineGraph+nL+nL+tab+tab1}Car Travel Information{nL+tab+tab+lineGraph}")
```

**Subsection:**
```python
print(f"{tab+tab}Acceleration applied:{nL+tab+tab+shortBar}")
```

**Data Row:**
```python
print(f"{tab+tab1}Accelerate #{count+1}:{tab}Increase by 5 mph{tab}Current speed: {speed}mpg")
```

**Summary Line:**
```python
print(f"{tab+tab+lineGraph+nL+tab+tab}Chevy Final Speed:{tab}{speed}mpg")
```

**RULES:**
- ALWAYS use constants, NEVER hardcode `\n` or spaces
- Import at top of class files: `nL, tab, tab1, lineGraph, shortBar, medBar = displayLabels.nL, ...`
- Concatenate with `+` operator
- `tab` for base indentation, `tab1` for sub-indentation
- `lineGraph` for major sections, `medBar` for titles, `shortBar` for subsections

---

## 9. VALIDATION PATTERNS

### Standard Validation Setup:
```python
v=V=typeValidation.validateInput
```

### Basic Validation Usage:
```python
accelerated:int = v(int, f"{nL+tab+tab}How many times did you accelerate? ")
braked:int = v(int, f"{tab+tab}How many times did you brake? ")
```

### Validation with Range Checking:
```python
while True:
    accelerated:int = v(int,f"{nL+tab+tab}How many times did you accelerate? ")
    if accelerated <0:
        os.system('cls')
        print('\tCan you do that in real life???')
        input()
        os.system('cls')
        START()
        self.printCarInfo(year, make)
    elif accelerated == 0:
        os.system('cls')
        print('\tYOU JUST WANT TO SIT STILL??')
        input()
        os.system('cls')
        START()
        self.printCarInfo(year, make)
        print(f"{tab+tab}How many times did you accelerate? {accelerated}")  
    elif accelerated >0:
        break
```

**VALIDATION RULES:**

1. **Use `v()` shorthand:**
   ```python
   value = v(int, "prompt")  # NOT validateInput()
   ```

2. **Type hint variables:**
   ```python
   accelerated:int = v(int, prompt)
   ```

3. **Validation Loop Pattern:**
   ```python
   while True:
       value = v(datatype, prompt)
       if <invalid_condition>:
           os.system('cls')
           print('\tError message')
           input()
           os.system('cls')
           START()
           # Redisplay context
       elif <valid_condition>:
           break
   ```

4. **Error Flow:**
   - Clear screen
   - Show error message
   - Wait for user acknowledgment (`input()`)
   - Clear again
   - Redisplay START banner
   - Redisplay previous data
   - Loop back

5. **Custom Error Messages:**
   - Use tab prefix: `print('\tCan you do that in real life???')`
   - Conversational tone
   - Specific to validation failure

---

## 10. MENU SYSTEM PATTERNS

### Menu Class Pattern (from CarMenu):

```python
class CarMenu():

    def __init__(self):
        self.carMakeYear:list
        self.choices:list
        self.choice:int

    # Getters/setters...

    def Start(self):
        carMakeYear = []
        choices = {}

        with open('data.txt', 'r') as file:
            carList:dict = (eval(str(file.read())))

        for car in carList:
            carMakeYear.append([carList[car]['year'], carList[car]['make'], car])
        carMakeYear.sort()

        for index, car in enumerate(carMakeYear, start=1):
            choices[index] = car

        self.set_choices(choices)
        return self.Provide()
        
    def Provide(self):
        choices = self.get_choices()

        while True:
            print('\n\tPlease choose an option:\n')

            for num in choices:
                year = choices[num][0]
                make = choices[num][1]
                model = choices[num][2]
                print(f"\t{num}) {year} {make}: {model}")

            try:
                choice = int(input('\n\tEnter the number associated: '))
            except ValueError:
                os.system('cls')
                print('\tPlease only enter numbers for a choice', flush=True)
                input('\n\tPress Enter to continue...')
                os.system('cls')
                continue
            
            if choice not in choices:
                os.system('cls')
                print('\tNot an option', flush=True)
                input('\n\tPress Enter to continue...')
                os.system('cls')
                continue
            
            # Get selection details
            year = choices[choice][0]
            make = choices[choice][1]
            model = choices[choice][2]
            os.system('cls')
            print(f"\n\tYou chose: {year} {make} {model}", flush=True)
            input('\n\tPress Enter to continue...')
            self.set_choice(choice)
            return choices[choice]
```

**MENU SYSTEM RULES:**

1. **Two-Method Pattern:**
   - `Start()`: Load/process data, return `Provide()`
   - `Provide()`: Display menu, get input, validate, return selection

2. **Data Structure:**
   - Use dictionary with integer keys: `{1: data, 2: data, ...}`
   - Store in instance variable via setter

3. **Menu Display:**
   - Tab-indented prompt: `print('\n\tPlease choose an option:\n')`
   - Numbered options: `print(f"\t{num}) {year} {make}: {model}")`
   - Tab-indented input prompt

4. **Validation:**
   - Try/except for ValueError (non-integer input)
   - Check if choice in dictionary keys
   - Clear screen and show error
   - Use `flush=True` for immediate display
   - Wait for Enter: `input('\n\tPress Enter to continue...')`

5. **Confirmation:**
   - Show selected item
   - Wait for Enter to proceed
   - Return data structure

---

## 11. FILE READING PATTERNS

### Reading Dictionary Data:
```python
with open('data.txt', 'r') as file:
    carList:dict = (eval(str(file.read())))
```

**RULES:**
- Use `with open()` context manager
- Read mode: `'r'`
- Use `eval(str(file.read()))` for dictionary files
- Type hint the result: `carList:dict`
- File in same directory as script

### Data File Format (data.txt):
```python
{
    'Model Name': {
        'field1': value1,
        'field2': value2,
        'year': 2024,
        'make': 'Brand'
    },
    'Another Model': {
        # ...
    }
}
```

**DATA FILE RULES:**
- Valid Python dictionary syntax
- String keys (model names)
- Nested dictionaries for attributes
- Consistent field names across all entries
- Properly quoted strings
- No trailing commas after last entry

---

## 12. LOOP VALIDATION PATTERNS

### Negative Number Validation:
```python
while True:
    value = v(int, prompt)
    if value < 0:
        os.system('cls')
        print('\tCan you do that in real life???')
        input()
        os.system('cls')
        START()
        # Redisplay context
    elif value >= 0:
        break
```

### Zero Value Validation:
```python
while True:
    value = v(int, prompt)
    if value == 0:
        os.system('cls')
        print('\tYOU JUST WANT TO SIT STILL??')
        input()
        os.system('cls')
        START()
        # Redisplay context
        print(f"Previous value: {previous}")
    elif value > 0:
        break
```

### Relational Validation (comparing inputs):
```python
while True:
    braked = v(int, prompt)
    if braked < 0:
        # Error flow
    elif braked > accelerated:
        os.system('cls')
        print(f"\tYou can\'t break less than the times you accelerated: {accelerated}.")
        input()
        os.system('cls')
        START()
        # Redisplay context
    elif braked >= 0:
        break
```

**LOOP VALIDATION RULES:**
1. Always use `while True:` with explicit `break`
2. Clear screen before showing error (`os.system('cls')`)
3. Show error message
4. Wait for user (`input()`)
5. Clear screen again
6. Redisplay START banner
7. Redisplay any previous context/values
8. Continue loop (no break on error)

---

## 13. FUNCTION/METHOD NAMING

### Naming Conventions from Project_09:

**Main Entry Points:**
- `main()` - lowercase, orchestrates main file
- `Start()` - PascalCase, initializes classes
- `Provide()` - PascalCase, provides data/menu

**Constructors/Setters:**
- `Constructor()` - PascalCase, processes initialization data
- `set_variableName()` - snake_case prefix with camelCase
- `get_variableName()` - snake_case prefix with camelCase

**Display Methods:**
- `printCarInfo()` - camelCase, displays specific data
- `displayMenu()` - camelCase, shows menu

**Action Methods:**
- `Driving()` - PascalCase, major program flow
- `Accelerator()` - PascalCase, significant actions
- `Brake()` - PascalCase, significant actions

**RULES:**
- main() always lowercase
- Major flow methods: PascalCase
- Utility methods: camelCase
- Getter/setter: snake_case prefix
- Descriptive names: `printCarInfo()` NOT `showCar()`

---

## 14. DOCUMENTATION STANDARDS

### File-Level Documentation Block:
```python
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   REQUIREMENTS                                              |
|_____________________________________________________________|
|                                                             |
|  - Car Selection                                            |
|        - Load cars from data.txt                            |
|        - User selects a car from menu                       |
|    - Simulation                                             |
|        - User inputs acceleration count                     |
|        - User inputs brake count                            |
|        - Display speed changes (+5 mph / -5 mph)            |
|    - Display                                                |
|        - Car Information (Year, Make, Model)                |
|        - Acceleration Log                                   |
|        - Braking Log                                        |
|        - Final Speed                                        |
|_____________________________________________________________|
|                                                             |
|   FUNCTIONS                                                 |
|_____________________________________________________________|
|                                                             |
|    REQUIRED                                                 |
|        - main()               | Orchestrates                |
|                                                             |
|    IMPORTED                                                 |
|        - vehiclesClass        | Car & CarMenu Classes       |
|        - displayLabels        | UI Banners                  |
|                                                             |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
```

**DOCUMENTATION RULES:**
1. Multi-line string block after imports
2. Box-drawing with underscores and pipes
3. Two sections: REQUIREMENTS and FUNCTIONS
4. REQUIREMENTS: List major features with sub-bullets
5. FUNCTIONS: List required and imported functions with descriptions
6. Align pipes vertically
7. 60 characters wide minimum

### Module-Level Docstrings (MyClasses):
```python
"""
Module Name

Brief description of module purpose.

Public API (__all__):
    ```python
    ['func1', 'func2', 'var1']
    ```

Function Signatures:
    ```python
    func1(arg: type) -> returnType
    ```

Usage:
    from module import func1
    
    result = func1(value)

Author: Matthew Ochoa
Date: December 6, 2025
Version: 1.0
"""
```

### Inline Comments:
```python
# Single-line explanation of next code block
code_here()

# Add parent directory to path if running from ProjectClasses folder
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

**INLINE COMMENT RULES:**
- Use for complex logic explanations
- Place ABOVE the code being explained
- Start with `#` followed by space
- Complete sentences with proper grammar
- NOT for obvious code

---

## 15. FORBIDDEN PRACTICES

### ❌ NEVER DO THESE:

1. **NO EMOJIS - EVER:**
   ```python
   # ❌ FORBIDDEN
   print("✅ Success!")
   print("❌ Error!")
   print("🚗 Car selected")
   ```

2. **NO Multiple Separate Prints for Related Content:**
   ```python
   # ❌ FORBIDDEN
   print(f"{tab}Title")
   print(f"{tab}----------")
   print(f"{tab}Data: {value}")
   
   # ✅ REQUIRED
   print(f"{tab}Title{nL+tab}----------{nL+tab}Data: {value}")
   ```

3. **NO Hardcoded Newlines/Spaces:**
   ```python
   # ❌ FORBIDDEN
   print("\n\n    Title")
   print("    " + "----------")
   
   # ✅ REQUIRED
   print(f"{nL+nL+tab}Title{nL+tab+medBar}")
   ```

4. **NO Generic Variable Names:**
   ```python
   # ❌ FORBIDDEN
   x = 5
   temp = getData()
   data = []
   
   # ✅ REQUIRED
   accelerated = 5
   carSelection = getData()
   carMakeYear = []
   ```

5. **NO Wildcard Imports:**
   ```python
   # ❌ FORBIDDEN
   from displayLabels import *
   
   # ✅ REQUIRED
   from MyClasses import displayLabels
   nL, tab = displayLabels.nL, displayLabels.tab
   ```

6. **NO Direct validateInput Calls:**
   ```python
   # ❌ FORBIDDEN
   value = typeValidation.validateInput(int, prompt)
   
   # ✅ REQUIRED
   v=V=typeValidation.validateInput
   value = v(int, prompt)
   ```

7. **NO Logic in Main File:**
   ```python
   # ❌ FORBIDDEN - main file with loops/validation/logic
   def main():
       while True:
           # 50 lines of logic
   
   # ✅ REQUIRED - main file minimal
   def main():
       START()
       Vroom=Car()
       END()
   ```

8. **NO Missing Type Hints:**
   ```python
   # ❌ FORBIDDEN
   def Constructor(self, car):
   
   # ✅ REQUIRED
   def Constructor(self, car:list) -> tuple:
   ```

9. **NO Prints in Menu __init__:**
   ```python
   # ❌ FORBIDDEN
   def __init__(self):
       START()
       print("Menu initializing")
   
   # ✅ REQUIRED
   def __init__(self):
       self.choices:dict
       self.choice:int
   ```

10. **NO Break/Continue Without Validation:**
    ```python
    # ❌ FORBIDDEN
    while True:
        value = v(int, prompt)
        if value > 0:
            break  # No error handling for <=0
    
    # ✅ REQUIRED
    while True:
        value = v(int, prompt)
        if value <= 0:
            os.system('cls')
            print('\tError message')
            input()
            os.system('cls')
            START()
        elif value > 0:
            break
    ```

---

## 📊 CHECKLIST FOR NEW PROJECTS

### Before Writing Code:
- [ ] Created directory structure (00_IMPORT, 01_WORKING, 02_FINALS)
- [ ] Copied MyClasses folder to project
- [ ] Created ProjectClasses folder if needed
- [ ] Created data.txt if needed

### Main File (MJO_ProjectName.py):
- [ ] Header with correct date/status
- [ ] Import pattern matches Project_09
- [ ] Context object created correctly
- [ ] START/END extracted
- [ ] Documentation block with REQUIREMENTS/FUNCTIONS
- [ ] main() function minimal (START, class instantiation, END)
- [ ] main() called at bottom

### Class File (ProjectClasses/className.py):
- [ ] Header with correct date/status
- [ ] sys/os path manipulation included
- [ ] Import displayLabels and typeValidation
- [ ] Extract formatting constants explicitly
- [ ] Create v=V=typeValidation.validateInput shorthand
- [ ] __init__ drives program flow
- [ ] All methods use PascalCase or camelCase appropriately
- [ ] Getter/setter for all instance variables
- [ ] Type hints on all parameters

### Print Statements:
- [ ] No multiple print statements for related content
- [ ] All use formatting constants (nL, tab, medBar, etc.)
- [ ] Concatenated with + operator
- [ ] No hardcoded \n or spaces
- [ ] No emojis anywhere

### Validation:
- [ ] Using v() shorthand
- [ ] Type hints on validated variables
- [ ] while True loops with explicit break
- [ ] Error flow: cls → print → input → cls → START → redisplay
- [ ] Custom error messages with tab prefix

### Menu Systems:
- [ ] Separate menu class
- [ ] Start() method loads data
- [ ] Provide() method handles user interaction
- [ ] Dictionary with integer keys
- [ ] Try/except for ValueError
- [ ] Check if choice in keys
- [ ] Confirmation with flush=True

### Final Review:
- [ ] No generic variable names (x, temp, data)
- [ ] No wildcard imports
- [ ] All constants from displayLabels
- [ ] Class architecture matches Project_09
- [ ] Main file minimal, class file does heavy lifting
- [ ] Copied to 02_FINALS with MJO_ prefix

---

## 🔍 QUICK REFERENCE

**Import Pattern:**
```python
from MyClasses import displayLabels
from ProjectClasses import specificClass
ProjectN=displayLabels.Context(N, 'MM/DD/YYYY','NAME', 'Purpose!')
END, START = ProjectN.END, ProjectN.START
Class=specificClass.Class
```

**Class Pattern:**
```python
v=V=typeValidation.validateInput
nL, tab, tab1, lineGraph, shortBar, medBar = displayLabels.nL, ...

class MainClass:
    def __init__(self, param:type = default):
        self.param = param
        Helper=HelperClass()
        self.data=Helper.Start()
        self.Constructor(self.data)
        self.MainLogic()
```

**Print Pattern:**
```python
print(f"{tab+tab}Title{nL+tab+tab+medBar}")
print(f"{tab+tab}Data: {value}")
```

**Validation Pattern:**
```python
while True:
    value = v(datatype, prompt)
    if <invalid>:
        os.system('cls')
        print('\tError')
        input()
        os.system('cls')
        START()
    elif <valid>:
        break
```

---

**END OF STANDARDS DOCUMENT**

*These are ABSOLUTE REQUIREMENTS. Any deviation is incorrect.*

*Reference: Project_09 (MJO_Project_09.py, vehiclesClass.py)*

*Last Updated: December 12, 2025*
