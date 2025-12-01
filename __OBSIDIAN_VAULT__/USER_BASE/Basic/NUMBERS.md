# Domain: Numbers

## Overview
Python has three numeric types: `int` (integers), `float` (decimal numbers), and `complex` (complex numbers with real and imaginary parts). Python automatically handles type conversions and provides extensive math operations.

---

## Number Types

### Integer (int)
**What it is**: Whole numbers without decimal points, positive or negative, unlimited size.

**Examples**:
```python
# Positive integers
x = 100
large = 1000000000000000000000  # No size limit!

# Negative integers
y = -50

# Zero
z = 0

# Check type
print(type(x))  # <class 'int'>

# Different bases
binary = 0b1010      # Binary (base 2) = 10 in decimal
octal = 0o12         # Octal (base 8) = 10 in decimal
hexadecimal = 0xFF   # Hex (base 16) = 255 in decimal

print(binary)        # 10
print(octal)         # 10
print(hexadecimal)   # 255

# Convert to different bases
num = 255
print(bin(num))  # '0b11111111' (binary)
print(oct(num))  # '0o377' (octal)
print(hex(num))  # '0xff' (hex)

# Very large integers (no overflow!)
huge = 10**100  # 1 followed by 100 zeros
print(huge)     # Works perfectly!

# Integer division
result = 10 // 3  # Floor division
print(result)     # 3 (not 3.333...)
```

**Real-world Uses**:
```python
# Counting
student_count = 25
items_in_cart = 3

# IDs
user_id = 12345
transaction_id = 987654321

# Years, days, quantities
year = 2025
days_in_week = 7
total_quantity = 100

# Array indices
numbers = [10, 20, 30, 40]
first = numbers[0]  # Index is int

# Loop counters
for i in range(10):
    print(i)
```

---

### Float
**What it is**: Numbers with decimal points or in scientific notation.

**Examples**:
```python
# Decimal numbers
price = 19.99
pi = 3.14159
temperature = -5.5

# Check type
print(type(price))  # <class 'float'>

# Scientific notation
large = 3.5e4      # 3.5 × 10^4 = 35000.0
small = 1.2e-3     # 1.2 × 10^-3 = 0.0012

print(large)  # 35000.0
print(small)  # 0.0012

# Float precision (careful with comparisons!)
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 (floating point error!)

# Proper comparison
import math
if math.isclose(result, 0.3):
    print("Close enough!")  # This prints

# Special float values
positive_inf = float('inf')   # Infinity
negative_inf = float('-inf')  # Negative infinity
not_a_number = float('nan')   # Not a Number

print(positive_inf > 1000000)  # True
print(math.isinf(positive_inf))  # True
print(math.isnan(not_a_number))  # True

# Float formatting
value = 3.14159265359
print(f"{value:.2f}")   # 3.14 (2 decimals)
print(f"{value:.4f}")   # 3.1416 (4 decimals)
print(f"{value:10.2f}") # "      3.14" (width 10)
```

**Real-world Uses**:
```python
# Money (but consider decimal module for precision)
price = 19.99
tax_rate = 0.08
total = price * (1 + tax_rate)
print(f"${total:.2f}")  # $21.59

# Measurements
height = 5.9  # feet
weight = 165.5  # pounds
distance = 26.2  # miles

# Percentages
success_rate = 0.85
print(f"{success_rate:.1%}")  # 85.0%

# Scientific calculations
speed_of_light = 2.998e8  # meters/second
planck_constant = 6.626e-34  # joule-seconds

# Ratios
aspect_ratio = 16 / 9
print(f"{aspect_ratio:.2f}")  # 1.78
```

---

### Complex
**What it is**: Numbers with real and imaginary parts (a + bj).

**Examples**:
```python
# Create complex numbers
z1 = 3 + 4j
z2 = 2 - 1j
z3 = complex(3, 4)  # Same as 3 + 4j

# Check type
print(type(z1))  # <class 'complex'>

# Access parts
print(z1.real)  # 3.0
print(z1.imag)  # 4.0

# Operations
sum_result = z1 + z2
print(sum_result)  # (5+3j)

product = z1 * z2
print(product)  # (10+5j)

# Conjugate (flip sign of imaginary part)
conjugate = z1.conjugate()
print(conjugate)  # (3-4j)

# Absolute value (magnitude)
magnitude = abs(z1)
print(magnitude)  # 5.0 (sqrt(3² + 4²))

# Phase angle
import cmath
angle = cmath.phase(z1)
print(angle)  # 0.9272952180016122 (radians)

# Convert to polar form
r, theta = cmath.polar(z1)
print(f"r={r}, θ={theta}")  # r=5.0, θ=0.927...
```

**Real-world Uses**:
```python
# Electrical engineering (AC circuits)
voltage = 120 + 0j  # volts
impedance = 50 + 30j  # ohms
current = voltage / impedance
print(f"Current: {current:.2f}")

# Signal processing
import cmath
signal = 3 + 4j
amplitude = abs(signal)
phase = cmath.phase(signal)
print(f"Amp: {amplitude}, Phase: {phase}")

# Quantum mechanics (wave functions)
psi = 0.707 + 0.707j  # Quantum state

# Note: Most beginners won't use complex numbers
# They're for advanced math/engineering
```

---

## Number Operations

### Arithmetic Operations
```python
a = 10
b = 3

# Basic operations
print(a + b)   # 13 (addition)
print(a - b)   # 7 (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.3333... (division, always float)
print(a // b)  # 3 (floor division, rounds down)
print(a % b)   # 1 (modulo, remainder)
print(a ** b)  # 1000 (exponent, a to power of b)

# Negative numbers
print(-a)      # -10 (unary minus)
print(abs(-5)) # 5 (absolute value)

# Precedence (PEMDAS)
result = 2 + 3 * 4  # 14 (not 20)
result = (2 + 3) * 4  # 20 (use parentheses)

# Mixed types (int + float = float)
x = 5      # int
y = 2.5    # float
z = x + y  # 7.5 (float)
print(type(z))  # <class 'float'>

# Division always returns float
print(10 / 2)  # 5.0 (not 5)
print(type(10 / 2))  # <class 'float'>

# Use // for integer division
print(10 // 2)  # 5
print(type(10 // 2))  # <class 'int'>
```

---

### Assignment Operations
```python
# Compound assignment operators
x = 10

x += 5   # x = x + 5 (now 15)
x -= 3   # x = x - 3 (now 12)
x *= 2   # x = x * 2 (now 24)
x /= 4   # x = x / 4 (now 6.0, becomes float!)
x //= 2  # x = x // 2 (now 3.0)
x **= 2  # x = x ** 2 (now 9.0)
x %= 4   # x = x % 4 (now 1.0)

# Increment/decrement (Python doesn't have ++ or --)
count = 0
count += 1  # This is the way
count -= 1

# Multiple operations
x = 10
x = x + 5  # Verbose
x += 5     # Better

# Real-world example
total = 0
for price in [10.99, 5.50, 3.25]:
    total += price
print(f"Total: ${total:.2f}")  # Total: $19.74
```

---

### Comparison Operations
```python
a = 10
b = 5

# Comparisons (return True/False)
print(a == b)  # False (equal to)
print(a != b)  # True (not equal to)
print(a > b)   # True (greater than)
print(a < b)   # False (less than)
print(a >= b)  # True (greater than or equal)
print(a <= b)  # False (less than or equal)

# Chained comparisons
x = 15
print(0 < x < 20)  # True (x is between 0 and 20)
print(10 <= x <= 20)  # True

# Same as:
print(0 < x and x < 20)  # True

# Float comparison (be careful!)
a = 0.1 + 0.2
b = 0.3
print(a == b)  # False (floating point error!)
print(f"{a} vs {b}")  # 0.30000000000000004 vs 0.3

# Proper float comparison
import math
print(math.isclose(a, b))  # True

# Or use epsilon
epsilon = 1e-10
print(abs(a - b) < epsilon)  # True

# Comparing different types
print(5 == 5.0)  # True (values equal)
print(5 is 5.0)  # False (different types)
print(type(5) == type(5.0))  # False
```

---

### Built-in Math Functions
```python
# Absolute value
print(abs(-5))      # 5
print(abs(-3.5))    # 3.5
print(abs(3 + 4j))  # 5.0 (magnitude for complex)

# Power
print(pow(2, 3))    # 8 (2³)
print(pow(2, 3, 5)) # 3 (2³ mod 5)
print(2 ** 3)       # 8 (same as pow(2, 3))

# Round
print(round(3.7))      # 4
print(round(3.14159, 2))  # 3.14 (2 decimals)
print(round(125, -1))  # 120 (round to nearest 10)
print(round(125, -2))  # 100 (round to nearest 100)

# Max and Min
print(max(1, 5, 3, 9, 2))  # 9
print(min(1, 5, 3, 9, 2))  # 1
print(max([1, 5, 3, 9, 2]))  # 9 (also works with list)

# Sum
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15
print(sum(numbers, 10))  # 25 (start from 10)

# Divmod (quotient and remainder)
quotient, remainder = divmod(17, 5)
print(quotient, remainder)  # 3 1
# Same as: 17 // 5 = 3, 17 % 5 = 1
```

---

### Math Module
```python
import math

# Constants
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045
print(math.tau) # 6.283185307179586 (2π)
print(math.inf) # inf (infinity)
print(math.nan) # nan (not a number)

# Rounding functions
print(math.ceil(3.1))   # 4 (round up)
print(math.floor(3.9))  # 3 (round down)
print(math.trunc(3.9))  # 3 (truncate decimal)

# Power and logarithms
print(math.sqrt(16))    # 4.0 (square root)
print(math.pow(2, 3))   # 8.0 (2³)
print(math.exp(1))      # 2.718... (e¹)
print(math.log(10))     # 2.302... (natural log)
print(math.log10(100))  # 2.0 (log base 10)
print(math.log2(8))     # 3.0 (log base 2)

# Trigonometry (angles in radians)
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))            # 1.0
print(math.tan(math.pi / 4))  # 1.0

# Convert degrees to radians
angle_degrees = 90
angle_radians = math.radians(angle_degrees)
print(math.sin(angle_radians))  # 1.0

# Convert radians to degrees
print(math.degrees(math.pi))  # 180.0

# Hyperbolic functions
print(math.sinh(0))  # 0.0
print(math.cosh(0))  # 1.0
print(math.tanh(0))  # 0.0

# Other useful functions
print(math.factorial(5))  # 120 (5!)
print(math.gcd(48, 18))   # 6 (greatest common divisor)
print(math.isclose(0.1 + 0.2, 0.3))  # True
print(math.isfinite(5))   # True
print(math.isinf(math.inf))  # True
print(math.isnan(math.nan))  # True

# Combinations and permutations (Python 3.8+)
print(math.comb(5, 2))  # 10 (5 choose 2)
print(math.perm(5, 2))  # 20 (5 permute 2)
```

---

### Real-World Examples

**1. Financial Calculations**:
```python
# Calculate loan payment
principal = 10000  # Loan amount
rate = 0.05        # Annual interest rate (5%)
years = 5

# Monthly payment formula
monthly_rate = rate / 12
num_payments = years * 12
payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / \
          ((1 + monthly_rate)**num_payments - 1)

print(f"Monthly payment: ${payment:.2f}")

# Compound interest
initial = 1000
rate = 0.05
time = 10
final = initial * (1 + rate) ** time
print(f"After {time} years: ${final:.2f}")

# Sales tax
price = 19.99
tax_rate = 0.08
total = price * (1 + tax_rate)
print(f"Total with tax: ${total:.2f}")
```

**2. Statistics**:
```python
# Average
numbers = [85, 90, 78, 92, 88]
average = sum(numbers) / len(numbers)
print(f"Average: {average:.1f}")

# Median
sorted_nums = sorted(numbers)
n = len(sorted_nums)
if n % 2 == 0:
    median = (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
else:
    median = sorted_nums[n//2]
print(f"Median: {median}")

# Standard deviation
import math
mean = sum(numbers) / len(numbers)
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
std_dev = math.sqrt(variance)
print(f"Std Dev: {std_dev:.2f}")
```

**3. Geometry**:
```python
import math

# Circle
radius = 5
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")

# Distance between two points
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance:.2f}")  # 5.0

# Triangle
a, b = 3, 4
hypotenuse = math.hypot(a, b)  # Same as sqrt(a² + b²)
print(f"Hypotenuse: {hypotenuse:.2f}")  # 5.0
```

**4. Unit Conversions**:
```python
# Temperature
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Distance
miles = 10
kilometers = miles * 1.60934
print(f"{miles} miles = {kilometers:.2f} km")

# Weight
pounds = 150
kilograms = pounds * 0.453592
print(f"{pounds} lbs = {kilograms:.2f} kg")
```

**5. Gaming/Graphics**:
```python
import math

# Random number in range
import random
dice_roll = random.randint(1, 6)
print(f"Rolled: {dice_roll}")

# Angle between two points
x1, y1 = 0, 0
x2, y2 = 1, 1
angle = math.atan2(y2 - y1, x2 - x1)
angle_degrees = math.degrees(angle)
print(f"Angle: {angle_degrees}°")  # 45°

# Rotation
x, y = 10, 0
angle = math.radians(90)  # Rotate 90°
new_x = x * math.cos(angle) - y * math.sin(angle)
new_y = x * math.sin(angle) + y * math.cos(angle)
print(f"New position: ({new_x:.2f}, {new_y:.2f})")
```

---

## Type Conversion

### Between Number Types
```python
# Int to Float
x = 5
y = float(x)
print(y)        # 5.0
print(type(y))  # <class 'float'>

# Float to Int (truncates decimal)
x = 3.9
y = int(x)
print(y)        # 3 (not 4!)
print(type(y))  # <class 'int'>

# String to Number
x = "123"
y = int(x)      # 123
z = float(x)    # 123.0

x = "3.14"
y = float(x)    # 3.14
# z = int(x)    # Error! Can't convert "3.14" directly to int

# Must convert to float first
z = int(float(x))  # 3

# Number to String
x = 123
y = str(x)      # "123"
print(type(y))  # <class 'str'>

# Complex conversions
x = complex(3, 4)     # 3+4j
y = complex(5)        # 5+0j
z = complex("3+4j")   # 3+4j

# Can't directly convert complex to int/float
c = 3 + 4j
# x = int(c)    # Error!
# Use real or imag part
x = int(c.real)  # 3
```

### Error Handling
```python
# Handle invalid conversions
user_input = "abc"

try:
    number = int(user_input)
except ValueError:
    print("Invalid number!")  # This prints

# Check if string is numeric
value = "123"
if value.isdigit():
    number = int(value)
    print(number)  # 123

# For negative numbers and decimals
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print(is_number("123"))    # True
print(is_number("-45.6"))  # True
print(is_number("abc"))    # False
```

---

## Number Formatting

### F-strings (Python 3.6+)
```python
value = 1234.5678

# Basic formatting
print(f"{value}")           # 1234.5678

# Decimal places
print(f"{value:.2f}")       # 1234.57

# Width and alignment
print(f"{value:10.2f}")     # "   1234.57" (right align)
print(f"{value:<10.2f}")    # "1234.57   " (left align)
print(f"{value:^10.2f}")    # " 1234.57  " (center)

# Thousands separator
large = 1234567.89
print(f"{large:,.2f}")      # 1,234,567.89

# Percentage
ratio = 0.875
print(f"{ratio:.1%}")       # 87.5%

# Scientific notation
big = 123456789
print(f"{big:.2e}")         # 1.23e+08

# Binary, Octal, Hex
num = 255
print(f"{num:b}")           # 11111111 (binary)
print(f"{num:o}")           # 377 (octal)
print(f"{num:x}")           # ff (hex lowercase)
print(f"{num:X}")           # FF (hex uppercase)

# Sign
positive = 42
negative = -42
print(f"{positive:+d}")     # +42
print(f"{negative:+d}")     # -42

# Padding with zeros
num = 42
print(f"{num:05d}")         # 00042
```

### Format Method
```python
value = 1234.5678

print("{:.2f}".format(value))      # 1234.57
print("{:10.2f}".format(value))    # "   1234.57"
print("{:,.2f}".format(value))     # 1,234.57

# Multiple values
print("{} + {} = {}".format(5, 3, 8))
# 5 + 3 = 8

# By index
print("{0} + {1} = {2}".format(5, 3, 8))
# 5 + 3 = 8

# By name
print("{a} + {b} = {c}".format(a=5, b=3, c=8))
# 5 + 3 = 8
```

---

## Special Number Handling

### Infinity and NaN
```python
# Infinity
pos_inf = float('inf')
neg_inf = float('-inf')

print(pos_inf > 1000000)    # True
print(neg_inf < -1000000)   # True
print(pos_inf + 1)          # inf (still infinity)
print(pos_inf * 2)          # inf

# Check for infinity
import math
print(math.isinf(pos_inf))  # True
print(math.isfinite(5))     # True
print(math.isfinite(pos_inf))  # False

# NaN (Not a Number)
nan = float('nan')
print(nan == nan)           # False (NaN != NaN!)
print(math.isnan(nan))      # True

# Operations with NaN
print(nan + 5)              # nan
print(nan * 2)              # nan
```

### Precision and Rounding
```python
# Decimal module (for precise decimal arithmetic)
from decimal import Decimal, getcontext

# Float precision issues
result = 0.1 + 0.1 + 0.1
print(result)  # 0.30000000000000004

# Decimal precision (exact!)
result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(result)  # 0.3 (exact!)

# Set precision
getcontext().prec = 6
result = Decimal(1) / Decimal(7)
print(result)  # 0.142857

# Money calculations
price = Decimal('19.99')
quantity = Decimal('3')
total = price * quantity
print(f"${total}")  # $59.97

# Fractions module (for rational numbers)
from fractions import Fraction

# Create fractions
f1 = Fraction(1, 3)  # 1/3
f2 = Fraction(1, 6)  # 1/6

result = f1 + f2
print(result)  # 1/2 (exact!)

# From decimal
f = Fraction(0.5)
print(f)  # 1/2
```

---

## Quick Reference

### Number Types
```python
int: 42, -17, 0
float: 3.14, -0.5, 1e6
complex: 3+4j, 2-1j
```

### Operations
```python
+, -, *, /    # Basic
//, %, **     # Floor div, modulo, power
abs(), round()  # Built-in functions
```

### Math Module
```python
import math
math.pi, math.e
math.sqrt(), math.pow()
math.sin(), math.cos()
math.ceil(), math.floor()
```

### Conversion
```python
int(x)     # To integer
float(x)   # To float
complex(r, i)  # To complex
str(x)     # To string
```

### Formatting
```python
f"{value:.2f}"      # 2 decimals
f"{value:10.2f}"    # Width 10
f"{value:,.2f}"     # Thousands separator
f"{value:.1%}"      # Percentage
```

