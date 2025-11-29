# Data Types - int, float, str, bool

## 📍 **Metadata**
- **Source**: Multiple Classes - Type Evolution Oct20-29
- **Professor Style**: FOUNDATION - Type Safety Critical
- **Difficulty**: Beginner to Intermediate
- **Tags**: #concept/data-types #source/in-class #difficulty/beginner #exam/critical #prof-style/validation #pattern/type-conversion

## 💡 **Core Concept**
Python data types and type conversion as emphasized by Professor Ally Baba. Understanding data types is crucial for proper input validation, calculations, and program reliability. Professor treats type safety as a professional requirement, not optional.

## 🖥️ **In-Class Code Examples**

### **Basic Data Type Assignment (Oct22)**
```python
def main():
    # String data type
    studentName = 'Matthew Ochoa'
    firstName = 'Matthew'
    lastName = 'Ochoa'
    
    # Integer data type  
    age = 25
    creditHours = 15
    
    # Float data type
    gpa = 3.85
    tuitionCost = 2500.50
    
    # Boolean data type
    isEnrolled = True
    isGraduated = False
```
- **Naming**: Descriptive variable names for each type
- **Assignment**: Direct assignment with appropriate literals
- **Professional Context**: Real-world data representation

### **Type Conversion in Input Functions (Oct29 Evolution)**

#### **Early Approach (Inconsistent)**
```python
def getIntData(prompt):
    value = float(input(prompt))    # ERROR: Using float for int function!
    return value
```
- **Problem**: Function name says "int" but uses float()
- **Teaching Moment**: Highlights importance of consistency

#### **Corrected Approach (Oct29)**  
```python
def getIntegerData(prompt):
    value = int(input(prompt))      # CORRECT: Actually using int()
    return value

def getFloatData(prompt):
    value = float(input(prompt))    # Consistent with function name
    return value
    
def getStringData(prompt):
    value = input(prompt)           # No conversion needed for strings
    return value
```
- **Consistency**: Function names match conversion types
- **Reliability**: Proper type conversion for each data type
- **Professional Standards**: Clear, predictable behavior

### **Advanced Type Validation (Professor's Complete System)**
```python
def getValidatedInteger(prompt, minValue=None, maxValue=None):
    \"\"\"Get integer with complete validation\"\"\"
    while True:
        try:
            # Type conversion with error handling
            value = int(input(prompt))
            
            # Range validation
            if minValue is not None and value < minValue:
                print(f'\\tError: Must be at least {minValue}')
                continue
            if maxValue is not None and value > maxValue:
                print(f'\\tError: Cannot exceed {maxValue}')
                continue
                
            return value
            
        except ValueError:
            print('\\tError: Please enter a valid integer')
        except KeyboardInterrupt:
            return None

def getValidatedFloat(prompt, minValue=None, maxValue=None):
    \"\"\"Get float with complete validation\"\"\"
    while True:
        try:
            value = float(input(prompt))
            
            if minValue is not None and value < minValue:
                print(f'\\tError: Must be at least {minValue}')
                continue  
            if maxValue is not None and value > maxValue:
                print(f'\\tError: Cannot exceed {maxValue}')
                continue
                
            return value
            
        except ValueError:
            print('\\tError: Please enter a valid number')
```
- **Complete Validation**: Type checking + range checking
- **Error Handling**: Specific error messages for each type
- **Professional Implementation**: Enterprise-level input validation

### **Type Checking and Conversion Patterns**
```python
def processUserData():
    \"\"\"Demonstrate type checking and conversion\"\"\"
    # Get different data types
    name = getStringData('\\tEnter your name: ')
    age = getIntegerData('\\tEnter your age: ')
    gpa = getFloatData('\\tEnter your GPA: ')
    
    # Type checking (for validation)
    if isinstance(age, int) and age > 0:
        print(f'\\tValid age: {age}')
    
    # Type conversion for display
    ageString = str(age)
    gpaString = str(gpa)
    
    # Formatted output with type awareness
    print(f'\\tStudent: {name}')
    print(f'\\tAge: {age} years')           # int
    print(f'\\tGPA: {gpa:.2f}')             # float with formatting
    print(f'\\tEnrolled: {True}')           # boolean
```

## 🎯 **Professor's Approach**

### **Type Safety Philosophy**
- **Never assume input type** - Always convert explicitly
- **Validate after conversion** - Check ranges and reasonableness  
- **Handle conversion errors** - Use try/except for robustness
- **Be consistent** - Function names should match their behavior

### **Conversion Patterns**
- **String to Integer**: `int(input())` with ValueError handling
- **String to Float**: `float(input())` with ValueError handling
- **Numbers to String**: `str(value)` for display formatting
- **Boolean Logic**: Direct assignment or conditional results

### **Common Data Type Uses**
- **Strings**: Names, descriptions, user text
- **Integers**: Counts, ages, whole number calculations
- **Floats**: Money, measurements, decimal calculations  
- **Booleans**: Flags, status indicators, conditional results

## 🔗 **Related Concepts**
- [[Input-Output-Concept]] - Type conversion in input functions
- [[Error-Handling-Concept]] - ValueError handling for type conversion
- [[Variables-Concept]] - Type-appropriate variable naming
- [[Operators-Concept]] - Type-specific operations

## 📚 **Book Connection**
- **Chapter Reference**: Gaddis Chapter 2 - Variables and Assignment
- **Extension**: Professor adds comprehensive validation beyond book examples
- **Professional Standards**: Enterprise-level type safety practices

## ⚡ **Quick Reference**

### **Data Type Literals**
```python
# String literals
name = 'John Smith'          # Single quotes (professor's preference)
address = \"123 Main St\"     # Double quotes (acceptable)

# Integer literals  
age = 25                     # Positive integer
count = 0                    # Zero
negative = -10               # Negative integer

# Float literals
price = 19.99                # Decimal number
rate = 0.15                  # Percentage as decimal
scientific = 1.5e6           # Scientific notation (1,500,000)

# Boolean literals
isActive = True              # Boolean True
isCompleted = False          # Boolean False
```

### **Type Conversion Functions**
```python
# String to other types
int('25')        # Returns: 25 (integer)
float('19.99')   # Returns: 19.99 (float)
bool('True')     # Returns: True (boolean)

# Other types to string
str(25)          # Returns: '25'
str(19.99)       # Returns: '19.99'  
str(True)        # Returns: 'True'

# Numeric conversions
int(19.99)       # Returns: 19 (truncates decimal)
float(25)        # Returns: 25.0 (adds decimal)
```

### **Professor's Standard Input Functions (COPY FOR EXAMS)**
```python
def getIntegerData(prompt):
    \"\"\"Get validated integer input\"\"\"
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\\tError: Please enter a valid integer')

def getFloatData(prompt):
    \"\"\"Get validated float input\"\"\"
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\\tError: Please enter a valid number')

def getStringData(prompt):
    \"\"\"Get string input (no conversion needed)\"\"\"
    value = input(prompt).strip()  # Remove leading/trailing whitespace
    return value
```

### **Type Checking Patterns**
```python
# Check if value is specific type
if isinstance(value, int):
    print('Value is an integer')
    
if isinstance(value, float):
    print('Value is a float')
    
if isinstance(value, str):
    print('Value is a string')

# Check for numeric types
if isinstance(value, (int, float)):
    print('Value is numeric')
```

### **EXAM-CRITICAL TYPE REQUIREMENTS**

#### **Input Validation (ALWAYS Required)**
- ✅ **MUST use try/except** for int() and float() conversions
- ✅ **MUST validate ranges** after successful conversion  
- ✅ **MUST provide helpful error messages** for invalid input
- ❌ **NEVER use raw int(input())** without error handling

#### **Variable Assignment**
- ✅ **Use appropriate types** for data: int for counts, float for money
- ✅ **Descriptive names** that indicate both purpose and type
- ✅ **Consistent conversion** in utility functions
- ❌ **Never mix types** inappropriately (like using float for count variables)

#### **Display Formatting**
```python
# Integer display
print(f'Count: {count}')

# Float display (money)  
print(f'Price: ${price:.2f}')

# String display
print(f'Name: {name}')

# Boolean display
print(f'Active: {isActive}')
```

**EXAM SUCCESS TIP**: Professor expects PERFECT type safety. Every input conversion must be wrapped in try/except, and all numeric inputs must be range-validated. Missing type validation loses major points.