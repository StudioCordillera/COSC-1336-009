# Conditionals - IF/ELIF/ELSE Logic

## 📍 **Metadata**
- **Source**: Class Date Oct29 - Files 35-43 (Major Transition)
- **Professor Style**: CRITICAL - Decision-Making Foundation
- **Difficulty**: Intermediate - Logical Reasoning Required
- **Tags**: #concept/control-flow #source/in-class #difficulty/intermediate #exam/critical #prof-style/syntax #date/1029 #pattern/conditionals

## 💡 **Core Concept**
Conditional statements for decision-making in programs. Professor introduces IF statements as a major conceptual shift from linear programming to branching logic. This represents the evolution from basic scripting to true programming logic.

## 🖥️ **In-Class Code Examples**

### **Basic IF/ELSE Statement (File 35)**
```python
def main():
    value = getIntegerData('\\tEnter an integer: ')
    
    if (value>0):
        print('\\tValue is > 0')
    else:
        print('\\tValue is not > 0')
```
- **Syntax**: Parentheses around condition `(value>0)` 
- **Professor Preference**: Always use parentheses for clarity
- **Binary Logic**: Simple true/false decision making

### **Multi-Branch Conditionals (File 37)**
```python
def main():
    value = getIntegerData('\\tEnter an integer: ')
    
    if (value>0):
        print('\\tValue is > 0')
    elif(value == 0):
        print('\\tValue is equal to 0')
    else:
        print('\\tValue is < 0')

# Professor's Comprehensive Tracing:
# Trace: 52(22)>57(T)>58>70      # Positive value path
# Trace: 52(0)>57(F)>59(T)>60>70 # Zero value path  
# Trace: 52(-5)>57(F)>59(F)>61>62>70 # Negative value path
```
- **Complete Coverage**: All possible number scenarios handled
- **Tracing Notation**: Professor documents every execution path
- **Teaching Tool**: (T) = True, (F) = False conditions

### **Complex Logical Operations (File 40)**
```python
def main():
    value = getIntegerData('\\tEnter an integer: ')
    
    if (value % 5 == 0 and value % 7 == 0):
        print('\\tValue is a multiple of 5 & 7')
    else:
        print('\\tValue is not a multiple of 5 & 7')
```
- **Modulo Operator**: Using `%` for divisibility checking
- **Logical AND**: Compound condition requiring both parts true
- **Real-world Logic**: Mathematical relationships in programming

### **Range-Based Decision Logic (File 43)**
```python
def main():
    numberChecks = getIntegerData('\\tEnter number of checks: ')
    
    if (numberChecks >= 40):
        print('\\tPay .10')
    elif (numberChecks >= 20):
        print('\\tPay .15')
    else:
        print('\\tPay .20')
```
- **Business Logic**: Tiered pricing structure
- **Range Conditions**: Using >= for threshold-based decisions  
- **Cascading Logic**: Order matters in elif chains

### **Advanced Conditional Patterns (Professor's Style)**
```python
def validateAge(age):
    \"\"\"Validate age with comprehensive checking\"\"\"
    if (age < 0):
        return False, \"Age cannot be negative\"
    elif (age > 150):
        return False, \"Age seems unrealistic\"
    elif (age < 18):
        return True, \"Minor - parental consent required\"
    else:
        return True, \"Valid adult age\"

def main():
    age = getIntegerData('\\tEnter your age: ')
    isValid, message = validateAge(age)
    
    if isValid:
        print(f'\\tValid: {message}')
    else:
        print(f'\\tError: {message}')
```
- **Validation Logic**: Input checking with detailed feedback
- **Multiple Returns**: Different paths return different results
- **Professional Error Handling**: Meaningful user feedback

## 🎯 **Professor's Approach**

### **Syntax Preferences**
- **Always Use Parentheses**: `if (condition):` not `if condition:`
- **Explicit Conditions**: `if (value == 0):` not `if not value:`
- **Clear Spacing**: Blank lines around conditional blocks
- **Consistent Indentation**: 4 spaces for all nested code

### **Logical Patterns**
- **Complete Coverage**: Handle all possible cases
- **Positive First**: Check positive conditions before negative
- **Range Order**: Highest values first in cascading conditions
- **Explicit Comparison**: Use `== 0` rather than `not value`

### **Teaching Methodology**
- **Trace Documentation**: Map every execution path
- **Real-world Examples**: Business logic, mathematical relationships
- **Error Prevention**: Validate before processing
- **Professional Structure**: Separate validation from main logic

## 🔗 **Related Concepts**
- [[Operators-Concept]] - Comparison and logical operators
- [[Functions-Concept]] - Conditionals within function structure
- [[Error-Handling-Concept]] - Validation patterns
- [[Variables-Concept]] - Conditional assignment

## 📚 **Book Connection**
- **Chapter Reference**: Gaddis Chapter 3 - Decision Structures and Boolean Logic
- **Professor Enhancement**: Adds comprehensive tracing and professional error handling
- **Practical Application**: Real business scenarios beyond basic book examples

## ⚡ **Quick Reference**

### **Basic Conditional Template**
```python
if (condition):
    # action for true
else:
    # action for false
```

### **Multi-Branch Template**
```python
if (condition1):
    # first case
elif (condition2):
    # second case  
elif (condition3):
    # third case
else:
    # default case
```

### **Range-Based Template**
```python
if (value >= high_threshold):
    # highest tier
elif (value >= medium_threshold):
    # medium tier
elif (value >= low_threshold):
    # low tier  
else:
    # default tier
```

### **Validation Template**
```python
def validateInput(value):
    \"\"\"Comprehensive input validation\"\"\"
    if (value < minimum):
        return False, \"Value too low\"
    elif (value > maximum):
        return False, \"Value too high\"
    else:
        return True, \"Valid input\"
```

### **EXAM-CRITICAL CONDITIONAL PATTERNS**

#### **Comparison Operators (Always use parentheses)**
```python
if (x > y):      # Greater than
if (x < y):      # Less than  
if (x >= y):     # Greater than or equal
if (x <= y):     # Less than or equal
if (x == y):     # Equal to
if (x != y):     # Not equal to
```

#### **Logical Operators**
```python
if (x > 0 and y > 0):    # Both conditions must be true
if (x > 0 or y > 0):     # Either condition can be true
if not (x > 0):          # Negation (but prefer explicit comparison)
```

#### **Professor's Preferred Patterns**
- ✅ **CORRECT**: `if (value == 0):` 
- ❌ **AVOID**: `if not value:`
- ✅ **CORRECT**: `if (age >= 18):`
- ❌ **AVOID**: `if age >= 18:` (missing parentheses)
- ✅ **CORRECT**: Complete elif chains with final else
- ❌ **AVOID**: Missing edge cases

### **Range Logic Template (COPY FOR EXAMS)**
```python
def main():
    value = getIntegerData('\\tEnter value: ')
    
    # Handle all ranges (order matters!)
    if (value >= 90):
        grade = 'A'
    elif (value >= 80):
        grade = 'B'  
    elif (value >= 70):
        grade = 'C'
    elif (value >= 60):
        grade = 'D'
    else:
        grade = 'F'
        
    print(f'\\tGrade: {grade}')
```

**CRITICAL EXAM TIP**: Professor heavily emphasizes COMPLETE coverage of all logical possibilities. Missing an else clause or edge case will result in point deduction.