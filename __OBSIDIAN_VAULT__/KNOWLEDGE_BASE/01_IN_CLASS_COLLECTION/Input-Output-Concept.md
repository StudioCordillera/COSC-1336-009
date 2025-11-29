# Input/Output - User Interaction Patterns

## 📍 **Metadata**
- **Source**: Multiple Classes - Files from Oct22, Oct27, Oct29
- **Professor Style**: CRITICAL - Validation is Essential
- **Difficulty**: Intermediate - Requires Error Handling
- **Tags**: #concept/input-output #source/in-class #difficulty/intermediate #exam/critical #prof-style/validation #pattern/input-validation #code/template

## 💡 **Core Concept**
User input collection with comprehensive validation and error handling. Professor emphasizes that ALL user input must be validated and handled professionally. Input/Output is never just `input()` and `print()` - it requires defensive programming.

## 🖥️ **In-Class Code Examples**

### **Basic Input Pattern (Early Oct22)**
```python
def main():
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    
    print('Name: ', name)
    print('Age: ', age)
```
- **Initial Pattern**: Simple input without validation
- **Problem**: No type conversion or error checking

### **Improved Input with Type Conversion**
```python
def main():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))  # Convert to integer
    
    print('Name: ', name)
    print('Age: ', age)
```
- **Evolution**: Added type conversion
- **Risk**: Will crash on invalid input

### **Professor's Utility Functions (Oct29)**
```python
def getIntegerData(prompt):
    value = int(input(prompt))
    return value

def getFloatData(prompt):
    value = float(input(prompt))
    return value
    
def getStringData(prompt):
    value = input(prompt)
    return value

def main():
    age = getIntegerData('\tEnter your age: ')
    gpa = getFloatData('\tEnter your GPA: ')
    name = getStringData('\tEnter your name: ')
```
- **Professional Pattern**: Separate functions for each data type
- **Consistent Interface**: All functions use prompt parameter
- **Reusability**: Functions can be used throughout program

### **Advanced Input Validation (Professor's Style)**
```python
def getValidatedInteger(prompt, minValue=None, maxValue=None):
    while True:
        try:
            value = int(input(prompt))
            if minValue is not None and value < minValue:
                print(f'\tError: Must be at least {minValue}')
                continue
            if maxValue is not None and value > maxValue:
                print(f'\tError: Cannot exceed {maxValue}')
                continue
            return value
        except ValueError:
            print('\tError: Please enter a valid integer')
        except KeyboardInterrupt:
            print('\n\tProgram terminated by user')
            return None
```
- **Complete Validation**: Type checking, range validation, user termination
- **Professional Error Messages**: Clear, helpful feedback
- **Defensive Programming**: Handle all possible input scenarios

## 🎯 **Professor's Approach**

### **Input Validation Philosophy**
- **NEVER trust user input** - Always validate everything
- **Provide helpful error messages** - Tell user what went wrong
- **Allow graceful exit** - Handle Ctrl+C appropriately
- **Use loops for retry** - Let user try again on error

### **Common Patterns**
- **Utility Functions**: getIntegerData(), getFloatData(), getStringData()
- **Try/Except Blocks**: Catch ValueError for type conversion
- **While Loops**: Repeat input until valid
- **Range Checking**: Validate min/max values where appropriate

### **Formatting Standards**
- **Prompt Clarity**: Clear, specific prompts with colons
- **Tab Indentation**: Use `\t` for indented prompts and errors
- **Consistent Messaging**: Standard error message formats
- **Professional Output**: Clean, organized result display

## 🔗 **Related Concepts**
- [[Error-Handling-Concept]] - Exception management in input
- [[Data-Types-Concept]] - Type conversion functions
- [[Functions-Concept]] - Input utility functions
- [[Variables-Concept]] - Storing input in variables

## 📚 **Book Connection**
- **Chapter Reference**: Gaddis Chapter 2 - Input, Processing, Output
- **Gap Analysis**: Book shows basic input() - Professor requires validation
- **Professional Extension**: Professor adds enterprise-level error handling

## ⚡ **Quick Reference**

### **Professor's Standard Input Functions**
```python
def getIntegerData(prompt):
    """Standard integer input with validation"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\tError: Please enter a valid integer')

def getFloatData(prompt):
    """Standard float input with validation"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\tError: Please enter a valid number')

def getStringData(prompt):
    """Standard string input"""
    value = input(prompt).strip()
    return value
```

### **Input Validation Template**
```python
def getValidatedInput(prompt, dataType, minVal=None, maxVal=None):
    """Universal input validation template"""
    while True:
        try:
            if dataType == int:
                value = int(input(prompt))
            elif dataType == float:
                value = float(input(prompt))
            else:
                value = input(prompt).strip()
                
            # Range validation for numeric types
            if isinstance(value, (int, float)):
                if minVal is not None and value < minVal:
                    print(f'\tError: Must be at least {minVal}')
                    continue
                if maxVal is not None and value > maxVal:
                    print(f'\tError: Cannot exceed {maxVal}')
                    continue
                    
            return value
            
        except ValueError:
            print('\tError: Invalid input type')
        except KeyboardInterrupt:
            return None
```

### **EXAM-CRITICAL PATTERNS**
- ✅ **ALWAYS validate input** - Never use raw input() without validation
- ✅ **Use try/except** - Handle ValueError for type conversion  
- ✅ **Provide helpful errors** - Tell user what went wrong
- ✅ **Allow retry** - Use while loops for re-input
- ✅ **Handle interrupts** - Catch Ctrl+C gracefully
- ❌ **NEVER assume valid input** - Always defensive programming

### **Exam Template (COPY THIS)**
```python
def main():
    print('\n')
    print('=' * 50)
    print('PROGRAM TITLE')
    print('=' * 50)
    
    # Input with validation
    value = getIntegerData('\tEnter a number: ')
    
    # Processing
    result = value * 2
    
    # Output
    print(f'\tResult: {result}')
    print('\n\tProgram completed successfully!')
```

**CRITICAL FOR EXAMS**: Professor expects EVERY input to be validated. Raw input() without error handling will lose significant points.