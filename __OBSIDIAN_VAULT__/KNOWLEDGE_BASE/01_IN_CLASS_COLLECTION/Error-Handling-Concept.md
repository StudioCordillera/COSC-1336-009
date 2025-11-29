# Error Handling - Validation & Exception Management

## 📍 **Metadata**
- **Source**: Progressive Development Oct20-29 - Professor's Core Philosophy
- **Professor Style**: ABSOLUTELY CRITICAL - Defensive Programming
- **Difficulty**: Intermediate to Advanced - Professional Requirement
- **Tags**: #concept/error-handling #source/in-class #difficulty/intermediate #exam/critical #prof-style/validation #pattern/defensive-programming

## 💡 **Core Concept**
Comprehensive error handling and input validation as the cornerstone of Professor Ally Baba's programming philosophy. "NEVER trust user input" - every program must handle all possible error scenarios professionally. This represents the transition from student programming to enterprise-level software development.

## 🖥️ **In-Class Code Examples**

### **Evolution of Error Handling Awareness**

#### **Phase 1: No Error Handling (Early Oct22)**
```python
def main():
    age = int(input('Enter your age: '))        # DANGEROUS!
    income = float(input('Enter income: '))     # WILL CRASH!
    
    if age > 18:
        print('You are an adult')
```
- **Problem**: Any invalid input crashes the program
- **Learning Point**: Demonstrates why validation is essential

#### **Phase 2: Basic Try/Except (Late Oct22)**
```python
def getIntegerData(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print('Error: Invalid input')
        return None                             # Returns None on error
```
- **Improvement**: Prevents crashes but doesn't retry
- **Limitation**: Single attempt, not user-friendly

#### **Phase 3: Complete Validation Loop (Oct29)**
```python
def getIntegerData(prompt):
    \"\"\"Get validated integer input with retry capability\"\"\"
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\\tError: Please enter a valid integer')
        except KeyboardInterrupt:
            print('\\n\\tProgram terminated by user')
            return None
```
- **Professional Standard**: Loops until valid input or user exit
- **User Friendly**: Clear error messages and graceful termination

### **Professor's Complete Validation System**
```python
def getValidatedInteger(prompt, minValue=None, maxValue=None):
    \"\"\"Complete integer validation with range checking\"\"\"
    while True:
        try:
            # Type conversion with error handling
            value = int(input(prompt))
            
            # Range validation
            if minValue is not None and value < minValue:
                print(f'\\tError: Value must be at least {minValue}')
                continue
            if maxValue is not None and value > maxValue:
                print(f'\\tError: Value cannot exceed {maxValue}')
                continue
            
            # Success - return valid value
            return value
            
        except ValueError:
            print('\\tError: Please enter a valid integer')
        except KeyboardInterrupt:
            print('\\n\\tProgram terminated by user')
            return None
        except Exception as e:
            print(f'\\tUnexpected error: {e}')
            
def getValidatedFloat(prompt, minValue=None, maxValue=None):
    \"\"\"Complete float validation with range checking\"\"\"
    while True:
        try:
            value = float(input(prompt))
            
            if minValue is not None and value < minValue:
                print(f'\\tError: Value must be at least {minValue}')
                continue
            if maxValue is not None and value > maxValue:
                print(f'\\tError: Value cannot exceed {maxValue}')
                continue
                
            return value
            
        except ValueError:
            print('\\tError: Please enter a valid number')
        except KeyboardInterrupt:
            return None
```

### **Business Logic Error Handling**
```python
def calculateLoanPayment(principal, rate, years):
    \"\"\"Calculate loan payment with comprehensive error checking\"\"\"
    
    # Input validation
    if principal <= 0:
        raise ValueError(\"Principal must be positive\")
    if rate < 0:
        raise ValueError(\"Interest rate cannot be negative\")  
    if years <= 0:
        raise ValueError(\"Loan term must be positive\")
    
    # Division by zero protection
    if rate == 0:
        # Handle zero interest rate specially
        return principal / (years * 12)
    
    # Standard calculation
    monthlyRate = rate / 12
    numPayments = years * 12
    
    try:
        payment = principal * (monthlyRate * (1 + monthlyRate)**numPayments) / ((1 + monthlyRate)**numPayments - 1)
        return payment
    except (OverflowError, ZeroDivisionError) as e:
        raise ValueError(f\"Calculation error: {e}\")

def main():
    \"\"\"Main program with complete error handling\"\"\"
    try:
        principal = getValidatedFloat('\\tLoan amount: $', 1000, 1000000)
        if principal is None:  # User cancelled
            return
            
        rate = getValidatedFloat('\\tAnnual rate (decimal): ', 0, 0.50)
        if rate is None:
            return
            
        years = getValidatedInteger('\\tLoan term (years): ', 1, 50)
        if years is None:
            return
            
        payment = calculateLoanPayment(principal, rate, years)
        print(f'\\tMonthly payment: ${payment:.2f}')
        
    except ValueError as e:
        print(f'\\tValidation error: {e}')
    except Exception as e:
        print(f'\\tUnexpected error: {e}')
```

### **File and System Error Handling (Advanced)**
```python
def saveResults(data, filename):
    \"\"\"Save data with comprehensive error handling\"\"\"
    try:
        with open(filename, 'w') as file:
            file.write(str(data))
        print(f'\\tData saved successfully to {filename}')
        return True
        
    except PermissionError:
        print(f'\\tError: Permission denied to write {filename}')
        return False
    except FileNotFoundError:
        print(f'\\tError: Directory not found for {filename}')
        return False  
    except OSError as e:
        print(f'\\tSystem error: {e}')
        return False
    except Exception as e:
        print(f'\\tUnexpected file error: {e}')
        return False
```

## 🎯 **Professor's Approach**

### **Error Handling Philosophy**
- **DEFENSIVE PROGRAMMING**: Assume everything will go wrong
- **USER-FRIENDLY MESSAGES**: Tell user exactly what's wrong and how to fix it
- **GRACEFUL RECOVERY**: Always allow user to retry or exit cleanly
- **COMPREHENSIVE COVERAGE**: Handle type errors, range errors, system errors
- **PROFESSIONAL STANDARDS**: Never let program crash on user input

### **Validation Hierarchy**
1. **Type Validation**: Ensure correct data type (int, float, str)
2. **Range Validation**: Check min/max values for numeric input
3. **Business Logic**: Validate against business rules
4. **System Validation**: Handle file system and resource errors
5. **Graceful Exit**: Allow user to cancel/exit at any time

### **Error Message Standards**
- **Descriptive**: Tell user exactly what's wrong
- **Actionable**: Suggest how to correct the error
- **Consistent**: Use same format across all errors
- **Professional**: Appropriate tone for business software

## 🔗 **Related Concepts**
- [[Input-Output-Concept]] - Validation in input functions
- [[Data-Types-Concept]] - Type conversion error handling
- [[Functions-Concept]] - Error handling in function design
- [[Conditionals-Concept]] - Validation logic with if statements

## 📚 **Book Connection**
- **Chapter Reference**: Gaddis Chapter 6 - Exception Handling (Advanced)
- **Gap**: Book covers basic try/except - Professor requires comprehensive validation
- **Professional Extension**: Enterprise-level error handling and user experience

## ⚡ **Quick Reference**

### **Basic Exception Handling Template**
```python
try:
    # Code that might fail
    result = risky_operation()
except SpecificError:
    # Handle specific error type  
    print('Specific error message')
except Exception as e:
    # Handle any other error
    print(f'Unexpected error: {e}')
```

### **Professor's Standard Input Validation (COPY FOR EXAMS)**
```python
def getValidatedInput(prompt, dataType, minVal=None, maxVal=None):
    \"\"\"Universal input validation template\"\"\"
    while True:
        try:
            # Get input and convert type
            if dataType == int:
                value = int(input(prompt))
            elif dataType == float:
                value = float(input(prompt))  
            else:
                value = input(prompt).strip()
            
            # Range validation for numeric types
            if isinstance(value, (int, float)):
                if minVal is not None and value < minVal:
                    print(f'\\tError: Must be at least {minVal}')
                    continue
                if maxVal is not None and value > maxVal:
                    print(f'\\tError: Cannot exceed {maxVal}')
                    continue
            
            # Success
            return value
            
        except ValueError:
            print('\\tError: Invalid input type')
        except KeyboardInterrupt:
            print('\\n\\tProgram terminated by user')
            return None
        except Exception as e:
            print(f'\\tUnexpected error: {e}')
```

### **Common Error Types to Handle**
```python
# Type conversion errors
except ValueError:           # Invalid int() or float() conversion
    print('Invalid number format')

# User interruption
except KeyboardInterrupt:    # Ctrl+C pressed
    print('Program cancelled by user')
    return None

# Mathematical errors  
except ZeroDivisionError:    # Division by zero
    print('Cannot divide by zero')

except OverflowError:        # Number too large
    print('Number exceeds maximum value')

# File system errors
except FileNotFoundError:    # File doesn't exist
    print('File not found')
    
except PermissionError:      # No write permission
    print('Permission denied')

# Catch-all for unexpected errors
except Exception as e:       # Any other error
    print(f'Unexpected error: {e}')
```

### **EXAM-CRITICAL ERROR HANDLING PATTERNS**

#### **ALWAYS Required for Input**
```python
def main():
    # NEVER do this (will lose major points):
    # age = int(input('Enter age: '))
    
    # ALWAYS do this instead:
    age = getValidatedInteger('\\tEnter age: ', 0, 150)
    if age is None:  # Handle user cancellation
        print('\\tProgram cancelled')
        return
```

#### **Division Operations**
```python
def safeDivision(numerator, denominator):
    \"\"\"Safe division with error handling\"\"\"
    try:
        if denominator == 0:
            raise ValueError(\"Cannot divide by zero\")
        return numerator / denominator
    except (ValueError, TypeError) as e:
        print(f'\\tDivision error: {e}')
        return None
```

#### **Business Logic Validation**
```python
def validateBusinessRules(data):
    \"\"\"Validate against business requirements\"\"\"
    errors = []
    
    if data.age < 18:
        errors.append(\"Must be 18 or older\")
    if data.income < 20000:
        errors.append(\"Minimum income requirement not met\")
    if data.creditScore < 600:
        errors.append(\"Credit score too low\")
    
    if errors:
        for error in errors:
            print(f'\\tValidation error: {error}')
        return False
    return True
```

### **Professor's Error Handling Checklist (EXAM REQUIREMENTS)**
- ✅ **NEVER use raw input conversion** without try/except
- ✅ **ALWAYS provide retry loops** for user input
- ✅ **ALWAYS handle KeyboardInterrupt** for graceful exit
- ✅ **ALWAYS validate ranges** for numeric input  
- ✅ **ALWAYS use descriptive error messages**
- ✅ **ALWAYS check for division by zero** before dividing
- ✅ **ALWAYS return None or raise exception** on validation failure
- ❌ **NEVER let program crash** on invalid user input

**EXAM SUCCESS GUARANTEE**: Following Professor's error handling patterns is the difference between passing and failing. Every input MUST be validated, every operation MUST handle errors, every program MUST fail gracefully.