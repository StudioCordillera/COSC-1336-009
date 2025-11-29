# Operators - Arithmetic, Comparison & Logical

## 📍 **Metadata**
- **Source**: Multiple Classes - Operator Evolution Oct20-29
- **Professor Style**: ESSENTIAL - Foundation for All Logic
- **Difficulty**: Beginner to Intermediate
- **Tags**: #concept/operators #source/in-class #difficulty/beginner #exam/critical #prof-style/syntax #pattern/calculations

## 💡 **Core Concept**
Mathematical, comparison, and logical operators as used throughout Professor Ally Baba's course. Operators are the building blocks for calculations, decision-making, and program logic. Professor emphasizes proper syntax and order of operations in professional programming contexts.

## 🖥️ **In-Class Code Examples**

### **Arithmetic Operators (Oct22 - Basic Calculations)**
```python
def main():
    # Basic arithmetic operations
    length = 5
    width = 10
    area = length * width          # Multiplication
    
    hoursWorked = 40
    hourlyWage = 15.50
    grossPay = hoursWorked * hourlyWage    # Real-world multiplication
    
    taxRate = 0.15
    taxAmount = grossPay * taxRate         # Percentage calculation
    netPay = grossPay - taxAmount          # Subtraction
    
    print('Area: ', area)
    print('Gross Pay: $', grossPay)
    print('Tax Amount: $', taxAmount)  
    print('Net Pay: $', netPay)
```
- **Business Context**: Real payroll calculations using multiplication and subtraction
- **Professional Usage**: Meaningful variable names with arithmetic operations

### **Comparison Operators (Oct29 - Conditionals)**
```python
def main():
    value = getIntegerData('\\tEnter an integer: ')
    
    # Basic comparisons
    if (value > 0):                    # Greater than
        print('\\tValue is positive')
    elif (value < 0):                  # Less than
        print('\\tValue is negative')
    elif (value == 0):                 # Equal to
        print('\\tValue is zero')
    
    # Range checking
    age = getIntegerData('\\tEnter age: ')
    if (age >= 18):                    # Greater than or equal
        print('\\tAdult')
    elif (age >= 13):                  # Compound range checking
        print('\\tTeenager')  
    else:
        print('\\tChild')
```
- **Professor Style**: Always use parentheses around comparisons
- **Complete Coverage**: Handle all possible comparison cases

### **Logical Operators (Oct29 - Complex Conditions)**
```python
def main():
    value = getIntegerData('\\tEnter an integer: ')
    
    # Logical AND - both conditions must be true
    if (value % 5 == 0 and value % 7 == 0):
        print('\\tValue is divisible by both 5 and 7')
    
    # Logical OR - either condition can be true  
    if (value < 0 or value > 100):
        print('\\tValue is outside normal range')
    
    # Complex logical expressions
    age = getIntegerData('\\tEnter age: ')
    income = getFloatData('\\tEnter income: ')
    
    if (age >= 18 and income >= 30000):
        print('\\tQualified for loan')
    elif (age >= 21 or income >= 50000):
        print('\\tSpecial consideration')
    else:
        print('\\tNot qualified')
```
- **Business Logic**: Real-world qualification scenarios
- **Compound Conditions**: Multiple criteria evaluation

### **Modulo Operator (Oct29 - Advanced Usage)**
```python
def main():
    number = getIntegerData('\\tEnter a number: ')
    
    # Check if even or odd
    if (number % 2 == 0):
        print('\\tNumber is even')
    else:
        print('\\tNumber is odd')
    
    # Check divisibility
    if (number % 5 == 0):
        print('\\tDivisible by 5')
    
    # Multiple divisibility (complex condition)
    if (number % 3 == 0 and number % 7 == 0):
        print('\\tDivisible by both 3 and 7')
```
- **Mathematical Concepts**: Divisibility and remainder operations
- **Professor Pattern**: Modulo used extensively for condition checking

### **Assignment vs Comparison (Critical Distinction)**
```python
def main():
    # ASSIGNMENT (single =)
    age = 25                       # Assigns value 25 to age
    name = 'John'                  # Assigns string to name
    total = price + tax            # Assigns calculation result
    
    # COMPARISON (double ==)
    if (age == 25):                # Checks if age equals 25
        print('Age is 25')
    
    if (name == 'John'):           # Checks if name equals 'John'  
        print('Name is John')
    
    # COMMON ERROR - Using = in conditions
    # if (age = 25):               # ERROR! This is assignment, not comparison
    # CORRECT:
    if (age == 25):                # This compares age to 25
```
- **Critical Distinction**: Assignment (=) vs Comparison (==)
- **Common Student Error**: Using = instead of == in conditions

## 🎯 **Professor's Approach**

### **Syntax Preferences**
- **Parentheses Required**: Always `if (condition)` not `if condition`
- **Spacing**: Clear spacing around operators `a + b` not `a+b`
- **Explicit Comparisons**: `if (value == 0)` not `if not value`
- **Professional Context**: Use operators in business/real-world scenarios

### **Order of Operations**
1. **Parentheses**: `()`
2. **Exponentiation**: `**`  
3. **Multiplication/Division/Modulo**: `*`, `/`, `//`, `%`
4. **Addition/Subtraction**: `+`, `-`
5. **Comparisons**: `<`, `>`, `<=`, `>=`, `==`, `!=`
6. **Logical AND**: `and`
7. **Logical OR**: `or`

### **Common Patterns**
- **Calculation Chains**: Build complex results step by step
- **Range Validation**: Use comparison operators for input checking
- **Business Logic**: Apply operators to real-world scenarios
- **Error Prevention**: Validate before using operators (division by zero)

## 🔗 **Related Concepts**
- [[Data-Types-Concept]] - Operator behavior with different types
- [[Conditionals-Concept]] - Comparison operators in if statements
- [[Variables-Concept]] - Assignment operators with variables
- [[Error-Handling-Concept]] - Division by zero prevention

## 📚 **Book Connection**
- **Chapter Reference**: Gaddis Chapter 2 - Variables and Assignment (arithmetic)
- **Chapter Reference**: Gaddis Chapter 3 - Decision Structures (comparison/logical)
- **Professor Enhancement**: Real business applications of all operator types

## ⚡ **Quick Reference**

### **Arithmetic Operators**
```python
result = a + b        # Addition
result = a - b        # Subtraction  
result = a * b        # Multiplication
result = a / b        # Division (float result)
result = a // b       # Floor division (integer result)
result = a % b        # Modulo (remainder)
result = a ** b       # Exponentiation (a to power of b)
```

### **Comparison Operators**
```python
if (a > b):          # Greater than
if (a < b):          # Less than
if (a >= b):         # Greater than or equal to
if (a <= b):         # Less than or equal to  
if (a == b):         # Equal to
if (a != b):         # Not equal to
```

### **Logical Operators**
```python
if (condition1 and condition2):    # Both must be true
if (condition1 or condition2):     # Either can be true
if not condition:                  # Negation (opposite)
```

### **Assignment Operators**
```python
x = 10              # Basic assignment
x += 5              # x = x + 5 (compound assignment)
x -= 3              # x = x - 3
x *= 2              # x = x * 2  
x /= 4              # x = x / 4
x %= 3              # x = x % 3
```

### **EXAM-CRITICAL OPERATOR PATTERNS**

#### **Business Calculation Template**
```python
def calculatePayroll():
    hoursWorked = getFloatData('\\tEnter hours: ')
    hourlyRate = getFloatData('\\tEnter rate: $')
    
    # Basic calculation
    grossPay = hoursWorked * hourlyRate
    
    # Tax calculations
    taxRate = 0.15
    taxAmount = grossPay * taxRate
    netPay = grossPay - taxAmount
    
    # Overtime calculation (if applicable)
    if (hoursWorked > 40):
        overtimeHours = hoursWorked - 40
        overtimePay = overtimeHours * hourlyRate * 1.5
        grossPay += overtimePay
```

#### **Validation with Operators**  
```python
def validateInput(value):
    # Range checking
    if (value < 0 or value > 100):
        return False, \"Value out of range\"
    
    # Divisibility checking  
    if (value % 5 != 0):
        return False, \"Must be multiple of 5\"
    
    # Complex validation
    if (value >= 18 and value <= 65):
        return True, \"Valid working age\"
    else:
        return False, \"Outside working age range\"
```

#### **Professor's Modulo Patterns (HIGH EXAM PROBABILITY)**
```python
# Even/Odd checking
if (number % 2 == 0):
    print('Even')
else:
    print('Odd')

# Divisibility testing
if (number % 5 == 0):
    print('Divisible by 5')

# Multiple criteria  
if (number % 3 == 0 and number % 5 == 0):
    print('Divisible by both 3 and 5')
```

### **Common Operator Errors (AVOID ON EXAM)**
- ❌ **Assignment in condition**: `if (x = 5)` (should be `==`)
- ❌ **Missing parentheses**: `if x > 5` (should be `if (x > 5)`)
- ❌ **Division by zero**: No validation before dividing
- ❌ **Wrong operator precedence**: Not using parentheses for clarity
- ✅ **CORRECT**: Always use parentheses, validate inputs, use appropriate operators

**EXAM SUCCESS TIP**: Professor tests operator precedence and syntax heavily. Always use parentheses for clarity, validate before mathematical operations, and distinguish assignment (=) from comparison (==).