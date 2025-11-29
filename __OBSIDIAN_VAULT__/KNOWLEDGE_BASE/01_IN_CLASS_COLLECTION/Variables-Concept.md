# Variables - Declaration & Assignment

## 📍 **Metadata**
- **Source**: Class Date Oct 22 - Files 05-10  
- **Professor Style**: High Priority - Core Foundation
- **Difficulty**: Beginner - Essential Programming Concept
- **Tags**: #concept/variables #source/in-class #difficulty/beginner #exam/critical #prof-style/naming #date/1022 #code/snippet

## 💡 **Core Concept**
Variable declaration, assignment, and naming conventions as taught by Professor Ally Baba. Emphasis on descriptive naming, proper initialization, and consistent usage patterns throughout programs.

## 🖥️ **In-Class Code Examples**

### **Basic Variable Assignment (File 05)**
```python
def main():
    firstName = 'Matthew'
    lastName = 'Ochoa'
    age = 25
    
    print('First Name: ', firstName)
    print('Last Name: ', lastName) 
    print('Age: ', age)
```
- **Naming Style**: camelCase for variables
- **Data Types**: String and integer assignment
- **Output Pattern**: Descriptive labels with values

### **Calculation Variables (File 06)**  
```python
def main():
    length = 5
    width = 10
    area = length * width
    
    print('Length: ', length)
    print('Width: ', width)
    print('Area: ', area)
```
- **Calculation**: Variables used in mathematical operations
- **Descriptive Names**: length, width, area (not x, y, z)
- **Sequential Logic**: Input → Process → Output

### **Multiple Data Types (File 07)**
```python
def main():
    studentName = 'Matthew Ochoa'
    studentAge = 25
    gpa = 3.85
    isEnrolled = True
    
    print('Student Name: ', studentName)
    print('Age: ', studentAge)
    print('GPA: ', gpa)
    print('Enrolled: ', isEnrolled)
```
- **String**: studentName with full name
- **Integer**: studentAge for numeric age
- **Float**: gpa with decimal precision
- **Boolean**: isEnrolled for true/false status

### **Advanced Variable Usage (File 08)**
```python
def main():
    hoursWorked = 40
    hourlyWage = 15.50
    grossPay = hoursWorked * hourlyWage
    taxRate = 0.15
    taxAmount = grossPay * taxRate
    netPay = grossPay - taxAmount
    
    print('Hours Worked: ', hoursWorked)
    print('Hourly Wage: $', hourlyWage)
    print('Gross Pay: $', grossPay)
    print('Tax Rate: ', taxRate)
    print('Tax Amount: $', taxAmount)  
    print('Net Pay: $', netPay)
```
- **Business Logic**: Real-world payroll calculation
- **Chained Calculations**: Variables building on previous variables
- **Professional Naming**: Complete, descriptive variable names

## 🎯 **Professor's Approach**

### **Naming Convention Requirements**
- **camelCase**: firstName, lastName, grossPay
- **Descriptive Names**: Never use single letters (x, y, z)
- **Business Context**: hoursWorked, not hrs or h
- **Meaningful**: taxRate, not rate or tr

### **Common Patterns**
- **Initialize Before Use**: Always assign value immediately
- **Sequential Calculations**: Build complex results step by step
- **Consistent Naming**: Similar concepts use similar naming patterns
- **Output Labels**: Print descriptive text with variable values

### **Teaching Emphasis**
- **Readability**: Code should be self-documenting through variable names
- **Professional Standards**: Variables names should be business-appropriate
- **Maintenance**: Future programmers should understand variable purpose instantly

## 🔗 **Related Concepts**
- [[Data-Types-Concept]] - Variable type assignments
- [[Basic-Output-Concept]] - Displaying variable values
- [[Operators-Concept]] - Mathematical operations with variables
- [[Input-Output-Concept]] - User input stored in variables

## 📚 **Book Connection**
- **Chapter Reference**: Gaddis Chapter 2 - Variables and Assignment
- **Alignment**: Class examples follow book's variable concepts
- **Extension**: Professor emphasizes professional naming beyond basic book examples

## ⚡ **Quick Reference**

### **Variable Assignment Template**
```python
def main():
    # Descriptive variable names (camelCase)
    variableName = value          # Assignment
    result = var1 + var2          # Calculation
    
    # Output with labels
    print('Label: ', variableName)
    print('Result: ', result)
```

### **Data Type Examples**
```python
# String variables
firstName = 'John'
fullName = 'John Smith'

# Numeric variables  
age = 25                    # Integer
gpa = 3.75                  # Float
hourlyWage = 15.50         # Float

# Boolean variables
isEnrolled = True
isGraduated = False
```

### **Naming Conventions (CRITICAL FOR EXAMS)**
- ✅ **CORRECT**: firstName, hoursWorked, grossPay, taxRate
- ❌ **INCORRECT**: fn, hrs, gp, rate, x, y, z
- ✅ **Pattern**: Use complete words, camelCase, business context
- ❌ **Never**: Single letters, abbreviations, unclear names

### **Exam Application**
Professor HEAVILY penalizes poor variable naming. Always use descriptive, professional variable names that clearly indicate their purpose in business context.