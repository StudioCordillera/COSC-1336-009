# FRACTIONS_MODULE

## Core Definition
**Fractions** provide exact rational number arithmetic in Python. The `fractions` module implements the `Fraction` class for representing and manipulating rational numbers as numerator/denominator pairs, avoiding floating-point precision errors.

**Tags**: #fractions #rational-numbers #exact-arithmetic #numeric #mathematics

---

## COMPLETE FRACTIONS QUICK REFERENCE

### FRACTIONS METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# FRACTION CREATION
# ═══════════════════════════════════════════════════════════════════════════
Fraction(numerator, denominator)     # Two integers | Create fraction | Returns Fraction object
Fraction(numerator)                  # Single integer | Create whole number fraction | Returns Fraction (n/1)
Fraction(float)                      # Float | Convert to exact fraction | Returns Fraction object
Fraction(decimal)                    # Decimal | Convert to exact fraction | Returns Fraction object
Fraction(string)                     # String | Parse fraction from string | Returns Fraction object
Fraction.from_float(float)           # Float | Explicit conversion | Returns Fraction object
Fraction.from_decimal(decimal)       # Decimal | Explicit conversion | Returns Fraction object
Fraction.from_number(number)         # Number (3.14+) | Universal constructor | Returns Fraction object

# ═══════════════════════════════════════════════════════════════════════════
# FRACTION PROPERTIES
# ═══════════════════════════════════════════════════════════════════════════
fraction.numerator                   # Fraction | Get numerator | Returns int (normalized)
fraction.denominator                 # Fraction | Get denominator | Returns int (normalized, always positive)
fraction.real                        # Fraction | Get real part | Returns Fraction (self)
fraction.imag                        # Fraction | Get imaginary part | Returns 0
fraction.as_integer_ratio()          # Fraction | Get (numerator, denominator) tuple | Returns (int, int)
fraction.is_integer()                # Fraction (3.12+) | Check if whole number | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# ARITHMETIC OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
frac1 + frac2                        # Two fractions | Addition | Returns new Fraction (exact sum)
frac1 - frac2                        # Two fractions | Subtraction | Returns new Fraction (exact difference)
frac1 * frac2                        # Two fractions | Multiplication | Returns new Fraction (exact product)
frac1 / frac2                        # Two fractions | Division | Returns new Fraction (exact quotient)
frac1 // frac2                       # Two fractions | Floor division | Returns int (floor quotient)
frac1 % frac2                        # Two fractions | Modulo | Returns Fraction (remainder)
divmod(frac1, frac2)                 # Two fractions | Quotient and remainder | Returns (int, Fraction)
frac ** power                        # Fraction and int | Exponentiation | Returns Fraction or float
pow(frac, power)                     # Fraction and int | Power | Returns Fraction or float
pow(frac, power, mod)                # Fraction, int, int | Modular exponentiation | Returns int or Fraction
+frac                                # Fraction | Unary plus | Returns Fraction (unchanged)
-frac                                # Fraction | Unary minus | Returns Fraction (negated)
abs(frac)                            # Fraction | Absolute value | Returns Fraction (positive)

# ═══════════════════════════════════════════════════════════════════════════
# COMPARISON OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
frac1 == frac2                       # Two fractions | Check equality | Returns True/False
frac1 != frac2                       # Two fractions | Check inequality | Returns True/False
frac1 < frac2                        # Two fractions | Less than | Returns True/False
frac1 > frac2                        # Two fractions | Greater than | Returns True/False
frac1 <= frac2                       # Two fractions | Less than or equal | Returns True/False
frac1 >= frac2                       # Two fractions | Greater than or equal | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# CONVERSION METHODS
# ═══════════════════════════════════════════════════════════════════════════
float(frac)                          # Fraction | Convert to float | Returns float (approximate)
int(frac)                            # Fraction | Convert to integer | Returns int (truncated)
round(frac)                          # Fraction | Round to nearest integer | Returns int
round(frac, ndigits)                 # Fraction | Round to n digits | Returns Fraction
math.floor(frac)                     # Fraction | Floor value | Returns int
math.ceil(frac)                      # Fraction | Ceiling value | Returns int
math.trunc(frac)                     # Fraction | Truncate to integer | Returns int
str(frac)                            # Fraction | Convert to string | Returns string "n/d"
repr(frac)                           # Fraction | Repr string | Returns string "Fraction(n, d)"

# ═══════════════════════════════════════════════════════════════════════════
# FRACTION METHODS
# ═══════════════════════════════════════════════════════════════════════════
frac.limit_denominator(max_d=1000000) # Fraction | Find closest fraction | Returns Fraction with denominator <= max_d
frac.conjugate()                     # Fraction | Complex conjugate | Returns Fraction (self for real numbers)
frac.__reduce__()                    # Fraction | Pickle support | Returns tuple for serialization
frac.__copy__()                      # Fraction | Shallow copy | Returns Fraction copy
frac.__deepcopy__(memo)              # Fraction | Deep copy | Returns Fraction copy

# ═══════════════════════════════════════════════════════════════════════════
# BOOLEAN OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
bool(frac)                           # Fraction | Check if non-zero | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# HASHING
# ═══════════════════════════════════════════════════════════════════════════
hash(frac)                           # Fraction | Get hash value | Returns int (for dict/set usage)

# ═══════════════════════════════════════════════════════════════════════════
# FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
f"{frac}"                            # Fraction | Default format | Returns string "n/d"
f"{frac:.2f}"                        # Fraction | Format as float | Returns formatted string
format(frac, format_spec)            # Fraction | Custom format | Returns formatted string
```

### COMMON OPERATION EXAMPLES

```python
from fractions import Fraction

# Creation
frac1 = Fraction(3, 4)               # → Fraction(3, 4)  = 3/4
frac2 = Fraction(1, 2)               # → Fraction(1, 2)  = 1/2
frac3 = Fraction(0.5)                # → Fraction(1, 2)  = 1/2
frac4 = Fraction('3/4')              # → Fraction(3, 4)  = 3/4
frac5 = Fraction('1.5')              # → Fraction(3, 2)  = 3/2
frac6 = Fraction(6, 8)               # → Fraction(3, 4)  = 3/4 (auto-reduced)

# Properties
frac1.numerator                      # → 3
frac1.denominator                    # → 4

# Arithmetic
Fraction(1, 2) + Fraction(1, 3)      # → Fraction(5, 6)  = 5/6
Fraction(3, 4) - Fraction(1, 4)      # → Fraction(1, 2)  = 1/2
Fraction(2, 3) * Fraction(3, 4)      # → Fraction(1, 2)  = 1/2
Fraction(1, 2) / Fraction(1, 4)      # → Fraction(2, 1)  = 2
Fraction(7, 3) // Fraction(2, 1)     # → 1 (floor division)
Fraction(7, 3) % Fraction(2, 1)      # → Fraction(1, 3)  = 1/3

# Comparison
Fraction(1, 2) == 0.5                # → True
Fraction(1, 2) < Fraction(3, 4)      # → True
Fraction(2, 3) > Fraction(1, 2)      # → True

# Conversion
float(Fraction(3, 4))                # → 0.75
int(Fraction(7, 3))                  # → 2 (truncates)
round(Fraction(7, 3))                # → 2

# Approximation
Fraction(3.14159).limit_denominator(100)  # → Fraction(22, 7) ≈ π
Fraction(2.71828).limit_denominator(10)   # → Fraction(19, 7) ≈ e
```

---

## DETAILED FRACTION OPERATIONS

### 1. CREATING FRACTIONS

```python
from fractions import Fraction

# From integers
f1 = Fraction(3, 4)                  # → 3/4
f2 = Fraction(5)                     # → 5/1 (whole number)
f3 = Fraction(-3, 4)                 # → -3/4 (negative)
f4 = Fraction(3, -4)                 # → -3/4 (normalized: negative in numerator)
f5 = Fraction(-3, -4)                # → 3/4 (both negative = positive)

# Auto-reduction
f6 = Fraction(6, 8)                  # → 3/4 (automatically reduced)
f7 = Fraction(100, 200)              # → 1/2 (reduced to lowest terms)
f8 = Fraction(0, 5)                  # → 0/1 (zero)

# From floats
f9 = Fraction(0.5)                   # → 1/2
f10 = Fraction(0.25)                 # → 1/4
f11 = Fraction(0.1)                  # → 3602879701896397/36028797018963968 (inexact!)
f12 = Fraction.from_float(0.5)       # → 1/2 (explicit method)

# From strings
f13 = Fraction('3/4')                # → 3/4
f14 = Fraction('1.5')                # → 3/2
f15 = Fraction('-.25')               # → -1/4
f16 = Fraction('7')                  # → 7/1
f17 = Fraction('22/7')               # → 22/7 (π approximation)
f18 = Fraction('  3 / 4  ')          # → 3/4 (whitespace ignored)

# From Decimal (for exact decimal arithmetic)
from decimal import Decimal
f19 = Fraction(Decimal('0.1'))       # → 1/10 (exact!)
f20 = Fraction.from_decimal(Decimal('3.14'))  # → 157/50

# From generic number (Python 3.14+)
f21 = Fraction.from_number(0.5)      # → 1/2 (accepts int, float, Decimal, Fraction)
f22 = Fraction.from_number(Decimal('0.25'))  # → 1/4

# Special cases
f23 = Fraction()                     # → 0/1 (default is zero)
f24 = Fraction(0, 1)                 # → 0/1 (zero)
# f25 = Fraction(1, 0)               # ZeroDivisionError (cannot divide by zero)

# Mixed operations (int, float)
f26 = Fraction(1, 2) + 1             # → 3/2 (int coerced to Fraction)
f27 = Fraction(1, 2) + 0.5           # → 1.0 (result is float)
```

### 2. ACCESSING PROPERTIES

```python
from fractions import Fraction

frac = Fraction(6, 8)                # Creates 3/4 (reduced)

# Numerator and denominator
print(frac.numerator)                # → 3 (always in lowest terms)
print(frac.denominator)              # → 4 (always positive, reduced)

# Denominator is always positive
neg_frac = Fraction(-6, 8)           # → -3/4
print(neg_frac.numerator)            # → -3 (negative)
print(neg_frac.denominator)          # → 4 (positive)

# Real and imaginary (for compatibility with complex numbers)
print(frac.real)                     # → Fraction(3, 4) (self)
print(frac.imag)                     # → 0 (no imaginary part)

# As integer ratio
ratio = frac.as_integer_ratio()      # → (3, 4)
n, d = frac.as_integer_ratio()
print(f"{n}/{d}")                    # → "3/4"

# Reconstruct fraction from ratio
new_frac = Fraction(*frac.as_integer_ratio())  # → Fraction(3, 4)

# Check if integer (Python 3.12+)
Fraction(4, 2).is_integer()          # → True (reduces to 2)
Fraction(5, 2).is_integer()          # → False (2.5)
Fraction(0, 1).is_integer()          # → True (0)
```

### 3. ARITHMETIC OPERATIONS

```python
from fractions import Fraction

# Basic arithmetic
a = Fraction(1, 2)                   # 1/2
b = Fraction(1, 3)                   # 1/3

# Addition (finds common denominator)
print(a + b)                         # → 5/6 (1/2 + 1/3 = 3/6 + 2/6 = 5/6)
print(Fraction(1, 4) + Fraction(1, 4))  # → 1/2

# Subtraction
print(a - b)                         # → 1/6 (1/2 - 1/3 = 3/6 - 2/6 = 1/6)
print(Fraction(3, 4) - Fraction(1, 4))  # → 1/2

# Multiplication
print(a * b)                         # → 1/6 (1/2 × 1/3 = 1/6)
print(Fraction(2, 3) * Fraction(3, 4))  # → 1/2 (reduced)

# Division
print(a / b)                         # → 3/2 (1/2 ÷ 1/3 = 1/2 × 3/1 = 3/2)
print(Fraction(1, 2) / Fraction(1, 4))  # → 2/1 = 2

# Floor division (returns int)
print(Fraction(7, 3) // Fraction(2, 1))  # → 1 (2.333... // 2 = 1)
print(Fraction(10, 3) // 2)          # → 1

# Modulo (returns Fraction)
print(Fraction(7, 3) % Fraction(2, 1))   # → 1/3 (remainder)
print(Fraction(10, 3) % 2)           # → 4/3

# Divmod (quotient and remainder)
q, r = divmod(Fraction(7, 3), 2)
print(q, r)                          # → 1 1/3

# Exponentiation
print(Fraction(1, 2) ** 2)           # → 1/4 (1/2 squared)
print(Fraction(2, 1) ** 3)           # → 8/1 = 8
print(Fraction(1, 2) ** -1)          # → 2/1 (reciprocal)
print(Fraction(4, 1) ** 0.5)         # → 2.0 (float for non-int exponent)

# Unary operations
print(+Fraction(3, 4))               # → 3/4 (unchanged)
print(-Fraction(3, 4))               # → -3/4 (negated)
print(abs(Fraction(-3, 4)))          # → 3/4 (absolute value)

# Mixed type operations
print(Fraction(1, 2) + 1)            # → 3/2 (int promoted to Fraction)
print(2 * Fraction(1, 3))            # → 2/3
print(Fraction(1, 2) + 0.5)          # → 1.0 (float result)
```

### 4. COMPARISON OPERATIONS

```python
from fractions import Fraction

# Equality
print(Fraction(1, 2) == Fraction(2, 4))      # → True (equivalent)
print(Fraction(1, 2) == 0.5)                 # → True (compares with float)
print(Fraction(1, 2) == Fraction(1, 3))      # → False

# Inequality
print(Fraction(1, 2) != Fraction(1, 3))      # → True
print(Fraction(2, 4) != Fraction(1, 2))      # → False (equivalent)

# Ordering
print(Fraction(1, 2) < Fraction(3, 4))       # → True
print(Fraction(3, 4) > Fraction(1, 2))       # → True
print(Fraction(1, 2) <= Fraction(2, 4))      # → True (equal)
print(Fraction(5, 6) >= Fraction(2, 3))      # → True

# Cross-comparison with different types
print(Fraction(1, 2) < 1)                    # → True
print(Fraction(3, 2) > 1)                    # → True
print(Fraction(1, 2) == 0.5)                 # → True
print(Fraction(1, 3) < 0.5)                  # → True

# Sorting fractions
fractions = [Fraction(3, 4), Fraction(1, 2), Fraction(2, 3), Fraction(1, 3)]
sorted_fracs = sorted(fractions)
print(sorted_fracs)                          # → [1/3, 1/2, 2/3, 3/4]

# Min/Max
print(min(Fraction(1, 2), Fraction(1, 3)))   # → 1/3
print(max(Fraction(3, 4), Fraction(2, 3)))   # → 3/4

# Boolean context
if Fraction(3, 4):
    print("Non-zero")                        # → "Non-zero"

if not Fraction(0, 1):
    print("Zero")                            # → "Zero"
```

### 5. CONVERSION METHODS

```python
from fractions import Fraction
import math

frac = Fraction(7, 3)                # 2.333...

# To float
print(float(frac))                   # → 2.3333333333333335

# To int (truncates toward zero)
print(int(frac))                     # → 2
print(int(Fraction(-7, 3)))          # → -2

# Rounding
print(round(frac))                   # → 2 (nearest integer)
print(round(Fraction(5, 2)))         # → 2 (banker's rounding: even)
print(round(Fraction(7, 2)))         # → 4

# Round to n digits (returns Fraction)
print(round(Fraction(22, 7), 2))     # → Fraction(157, 50) = 3.14

# Floor (largest int <= frac)
print(math.floor(frac))              # → 2
print(math.floor(Fraction(-7, 3)))   # → -3

# Ceiling (smallest int >= frac)
print(math.ceil(frac))               # → 3
print(math.ceil(Fraction(-7, 3)))    # → -2

# Truncate (remove fractional part)
print(math.trunc(frac))              # → 2
print(math.trunc(Fraction(-7, 3)))   # → -2

# To string
print(str(Fraction(3, 4)))           # → "3/4"
print(repr(Fraction(3, 4)))          # → "Fraction(3, 4)"

# Formatted output
frac = Fraction(3, 4)
print(f"{frac}")                     # → "3/4"
print(f"{float(frac):.2f}")          # → "0.75"
print(f"{float(frac):.1%}")          # → "75.0%"
```

### 6. APPROXIMATING FRACTIONS

```python
from fractions import Fraction
import math

# limit_denominator() - find closest fraction with small denominator

# Approximate π
pi = math.pi                         # 3.141592653589793
pi_frac = Fraction(pi)
print(pi_frac)                       # → Very large denominator!

# Limit to denominator <= 10
print(pi_frac.limit_denominator(10))       # → 22/7 (close approximation)
print(float(Fraction(22, 7)))              # → 3.142857... (error ~0.04%)

# Limit to denominator <= 100
print(pi_frac.limit_denominator(100))      # → 311/99 (better)
print(float(Fraction(311, 99)))            # → 3.14141... (error ~0.006%)

# Limit to denominator <= 1000
print(pi_frac.limit_denominator(1000))     # → 355/113 (excellent!)
print(float(Fraction(355, 113)))           # → 3.1415929... (error ~0.000008%)

# Approximate e (Euler's number)
e = math.e                           # 2.718281828459045
e_frac = Fraction(e).limit_denominator(10)
print(e_frac)                        # → 19/7 = 2.714...

# Approximate √2
sqrt2 = math.sqrt(2)                 # 1.4142135623730951
print(Fraction(sqrt2).limit_denominator(10))    # → 7/5 = 1.4
print(Fraction(sqrt2).limit_denominator(100))   # → 99/70 = 1.41428...
print(Fraction(sqrt2).limit_denominator(1000))  # → 665/470 = 1.41489...

# Practical use: simplifying measurement ratios
measurement = 3.14159
simple = Fraction(measurement).limit_denominator(32)
print(f"Measurement: {measurement}")
print(f"Simplified: {simple} = {float(simple):.5f}")
# Useful for woodworking, construction, etc.

# Convert float to readable fraction
def float_to_fraction(num, max_denominator=100):
    """Convert float to readable fraction"""
    return Fraction(num).limit_denominator(max_denominator)

print(float_to_fraction(0.333))      # → 1/3
print(float_to_fraction(0.666))      # → 2/3
print(float_to_fraction(0.125))      # → 1/8
print(float_to_fraction(0.375))      # → 3/8
```

### 7. WORKING WITH DECIMALS

```python
from fractions import Fraction
from decimal import Decimal

# Problem: 0.1 cannot be represented exactly in binary
print(Fraction(0.1))                 # → 3602879701896397/36028797018963968 (ugly!)
print(float(Fraction(0.1)))          # → 0.1 (but not exact internally)

# Solution: Use Decimal for exact decimal representation
print(Fraction(Decimal('0.1')))      # → 1/10 (exact!)

# Why this matters: financial calculations
price = 0.1
tax = 0.2
total_float = price + price + tax    # Floating point
total_frac = Fraction(Decimal('0.1')) + Fraction(Decimal('0.1')) + Fraction(Decimal('0.2'))

print(f"Float: {total_float}")       # → 0.4 (seems ok)
print(f"Fraction: {total_frac}")     # → 2/5 (exactly 0.4)
print(f"Are they equal? {total_float == float(total_frac)}")  # → True (lucky!)

# More complex example
values = [0.1] * 10
sum_float = sum(values)
sum_frac = sum(Fraction(Decimal('0.1')) for _ in range(10))

print(f"Float sum: {sum_float}")     # → 0.9999999999999999 (rounding error!)
print(f"Fraction sum: {sum_frac}")   # → 1 (exact!)
print(f"Equal? {sum_float == 1.0}")  # → False!

# Best practice for decimal arithmetic
def decimal_to_fraction(dec_string):
    """Convert decimal string to exact Fraction"""
    return Fraction(Decimal(dec_string))

# Financial calculations
price = decimal_to_fraction('19.99')
quantity = 3
tax_rate = decimal_to_fraction('0.08')

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: ${float(subtotal):.2f}")
print(f"Tax: ${float(tax):.2f}")
print(f"Total: ${float(total):.2f}")
```

### 8. ADVANCED OPERATIONS

```python
from fractions import Fraction
import math

# GCD and LCM with fractions
def gcd_fractions(f1, f2):
    """GCD of two fractions"""
    # GCD of a/b and c/d = GCD(a,c) / LCM(b,d)
    num_gcd = math.gcd(f1.numerator, f2.numerator)
    den_lcm = (f1.denominator * f2.denominator) // math.gcd(f1.denominator, f2.denominator)
    return Fraction(num_gcd, den_lcm)

print(gcd_fractions(Fraction(1, 2), Fraction(1, 3)))  # → 1/6

# Continued fractions
def to_continued_fraction(frac, max_terms=10):
    """Convert fraction to continued fraction representation"""
    result = []
    n, d = frac.numerator, frac.denominator
    
    for _ in range(max_terms):
        if d == 0:
            break
        q, r = divmod(n, d)
        result.append(q)
        n, d = d, r
    
    return result

print(to_continued_fraction(Fraction(22, 7)))     # → [3, 7] (represents 3 + 1/7)
print(to_continued_fraction(Fraction(355, 113)))  # → [3, 7, 16] (π approximation)

# Egyptian fractions (sum of unit fractions)
def to_egyptian_fraction(frac):
    """Convert fraction to sum of unit fractions (greedy algorithm)"""
    result = []
    n, d = frac.numerator, frac.denominator
    
    while n > 0:
        unit_d = -(-d // n)  # Ceiling division
        result.append(Fraction(1, unit_d))
        n = n * unit_d - d
        d = d * unit_d
    
    return result

print(to_egyptian_fraction(Fraction(3, 4)))   # → [1/2, 1/4]
print(to_egyptian_fraction(Fraction(5, 6)))   # → [1/2, 1/3]

# Mediant (for finding fractions between fractions)
def mediant(f1, f2):
    """Calculate mediant of two fractions"""
    return Fraction(f1.numerator + f2.numerator, 
                   f1.denominator + f2.denominator)

a = Fraction(1, 3)
b = Fraction(1, 2)
print(mediant(a, b))                          # → 2/5 (between 1/3 and 1/2)

# Reciprocal
def reciprocal(frac):
    """Get reciprocal of fraction"""
    if frac.numerator == 0:
        raise ZeroDivisionError("Cannot take reciprocal of zero")
    return Fraction(frac.denominator, frac.numerator)

print(reciprocal(Fraction(3, 4)))             # → 4/3
print(reciprocal(Fraction(5, 1)))             # → 1/5
```

### 9. HASHING AND COLLECTIONS

```python
from fractions import Fraction

# Fractions are hashable (can be dict keys or set members)
frac_dict = {
    Fraction(1, 2): "half",
    Fraction(1, 3): "third",
    Fraction(1, 4): "quarter"
}

print(frac_dict[Fraction(1, 2)])              # → "half"
print(frac_dict[Fraction(2, 4)])              # → "half" (reduced to 1/2)

# Sets of fractions
frac_set = {Fraction(1, 2), Fraction(2, 4), Fraction(1, 3)}
print(frac_set)                               # → {Fraction(1, 2), Fraction(1, 3)}
                                              # (2/4 and 1/2 are same)

# Equivalent fractions have same hash
print(hash(Fraction(1, 2)) == hash(Fraction(2, 4)))  # → True

# Fraction and equivalent float have same hash (when exact)
print(hash(Fraction(1, 2)) == hash(0.5))      # → True
print(Fraction(1, 2) == 0.5)                  # → True

# Counting with fractions
from collections import Counter

measurements = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 2), 
                Fraction(2, 4), Fraction(1, 3)]
counts = Counter(measurements)
print(counts)                                 # → {Fraction(1, 2): 3, Fraction(1, 3): 2}
```

### 10. PRACTICAL ALGORITHMS

```python
from fractions import Fraction

# Averaging fractions (exact)
def average_fractions(fractions):
    """Calculate exact average of fractions"""
    return sum(fractions, Fraction(0)) / len(fractions)

data = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)]
print(average_fractions(data))                # → 13/36

# Weighted average
def weighted_average(values, weights):
    """Calculate weighted average"""
    total_weight = sum(weights)
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    return weighted_sum / total_weight

grades = [Fraction(85, 100), Fraction(90, 100), Fraction(78, 100)]
weights = [Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)]
print(weighted_average(grades, weights))      # → 843/1000 = 0.843

# Simplifying ratios
def simplify_ratio(*numbers):
    """Simplify a ratio to lowest terms"""
    # Convert to fractions with common denominator
    fractions = [Fraction(n).limit_denominator() for n in numbers]
    
    # Find LCM of all denominators
    denominators = [f.denominator for f in fractions]
    lcm = denominators[0]
    for d in denominators[1:]:
        lcm = (lcm * d) // math.gcd(lcm, d)
    
    # Multiply to get integers
    integers = [int(f * lcm) for f in fractions]
    
    # Reduce by GCD
    from functools import reduce
    common_gcd = reduce(math.gcd, integers)
    return tuple(n // common_gcd for n in integers)

print(simplify_ratio(6, 8, 10))               # → (3, 4, 5)
print(simplify_ratio(0.5, 0.75, 1.0))         # → (2, 3, 4)

# Harmonic mean
def harmonic_mean(fractions):
    """Calculate harmonic mean of fractions"""
    n = len(fractions)
    reciprocal_sum = sum(Fraction(1) / f for f in fractions)
    return n / reciprocal_sum

speeds = [Fraction(60), Fraction(40), Fraction(80)]
print(harmonic_mean(speeds))                  # → 240/7 ≈ 34.29 mph

# Partial sums
def partial_sums(fractions):
    """Generate cumulative sum of fractions"""
    result = []
    total = Fraction(0)
    for f in fractions:
        total += f
        result.append(total)
    return result

series = [Fraction(1, 2), Fraction(1, 4), Fraction(1, 8)]
print(partial_sums(series))                   # → [1/2, 3/4, 7/8]
```

---

## PRACTICAL PROJECT PATTERNS

### Pattern 1: Exact Financial Calculations
```python
from fractions import Fraction
from decimal import Decimal

class ExactMoney:
    """Money class using Fractions for exact arithmetic"""
    
    def __init__(self, amount):
        if isinstance(amount, str):
            self.value = Fraction(Decimal(amount))
        else:
            self.value = Fraction(amount).limit_denominator(100)
    
    def __add__(self, other):
        return ExactMoney(self.value + other.value)
    
    def __mul__(self, multiplier):
        return ExactMoney(self.value * multiplier)
    
    def __str__(self):
        return f"${float(self.value):.2f}"
    
    def to_cents(self):
        """Convert to cents (no rounding errors)"""
        return int(self.value * 100)

# Usage
price = ExactMoney("19.99")
quantity = 3
total = price * quantity
print(f"Total: {total}")                      # → Total: $59.97
print(f"Cents: {total.to_cents()}")           # → Cents: 5997
```

### Pattern 2: Ratio and Proportion Problems
```python
from fractions import Fraction

def solve_proportion(a, b, c):
    """Solve a/b = c/x for x"""
    # x = (b * c) / a
    return (Fraction(b) * Fraction(c)) / Fraction(a)

# If 3 apples cost $2, how much do 7 apples cost?
result = solve_proportion(3, 2, 7)
print(f"7 apples cost ${float(result):.2f}")  # → $4.67

def scale_recipe(ingredients, original_servings, desired_servings):
    """Scale recipe quantities"""
    multiplier = Fraction(desired_servings, original_servings)
    return {item: qty * multiplier for item, qty in ingredients.items()}

original = {
    "flour": Fraction(2, 1),      # 2 cups
    "sugar": Fraction(1, 2),      # 1/2 cup
    "butter": Fraction(1, 4)      # 1/4 cup
}

scaled = scale_recipe(original, 4, 6)
for item, qty in scaled.items():
    print(f"{item}: {qty} cups")
# flour: 3 cups
# sugar: 3/4 cups
# butter: 3/8 cups
```

### Pattern 3: Music Theory (Note Frequencies)
```python
from fractions import Fraction
import math

# Musical intervals as frequency ratios
INTERVALS = {
    "unison": Fraction(1, 1),
    "minor_second": Fraction(16, 15),
    "major_second": Fraction(9, 8),
    "minor_third": Fraction(6, 5),
    "major_third": Fraction(5, 4),
    "perfect_fourth": Fraction(4, 3),
    "tritone": Fraction(45, 32),
    "perfect_fifth": Fraction(3, 2),
    "minor_sixth": Fraction(8, 5),
    "major_sixth": Fraction(5, 3),
    "minor_seventh": Fraction(16, 9),
    "major_seventh": Fraction(15, 8),
    "octave": Fraction(2, 1)
}

def calculate_frequency(base_freq, interval_name):
    """Calculate frequency of note at given interval"""
    ratio = INTERVALS[interval_name]
    return float(Fraction(base_freq) * ratio)

# A440 standard
a4 = 440
print(f"A4: {a4} Hz")
print(f"E5 (perfect fifth): {calculate_frequency(a4, 'perfect_fifth'):.2f} Hz")
print(f"A5 (octave): {calculate_frequency(a4, 'octave'):.2f} Hz")
```

### Pattern 4: Unit Conversion
```python
from fractions import Fraction

class Unit:
    """Exact unit conversion using fractions"""
    
    CONVERSIONS = {
        # Length
        ("inch", "foot"): Fraction(1, 12),
        ("foot", "yard"): Fraction(1, 3),
        ("yard", "mile"): Fraction(1, 1760),
        
        # Volume
        ("teaspoon", "tablespoon"): Fraction(1, 3),
        ("tablespoon", "cup"): Fraction(1, 16),
        ("cup", "gallon"): Fraction(1, 16),
    }
    
    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """Convert between units"""
        if from_unit == to_unit:
            return value
        
        # Direct conversion
        if (from_unit, to_unit) in cls.CONVERSIONS:
            return Fraction(value) * cls.CONVERSIONS[(from_unit, to_unit)]
        
        # Reverse conversion
        if (to_unit, from_unit) in cls.CONVERSIONS:
            return Fraction(value) / cls.CONVERSIONS[(to_unit, from_unit)]
        
        raise ValueError(f"Cannot convert {from_unit} to {to_unit}")

# Usage
result = Unit.convert(9, "inch", "foot")
print(f"9 inches = {result} feet")            # → 3/4 feet
print(f"9 inches = {float(result)} feet")     # → 0.75 feet
```

### Pattern 5: Probability Calculations
```python
from fractions import Fraction

class Probability:
    """Exact probability calculations"""
    
    def __init__(self, favorable, total):
        self.prob = Fraction(favorable, total)
    
    def complement(self):
        """P(not A) = 1 - P(A)"""
        return Probability(1 - self.prob.numerator, self.prob.denominator)
    
    def and_independent(self, other):
        """P(A and B) = P(A) × P(B) for independent events"""
        result = self.prob * other.prob
        return Probability(result.numerator, result.denominator)
    
    def or_mutually_exclusive(self, other):
        """P(A or B) = P(A) + P(B) for mutually exclusive events"""
        result = self.prob + other.prob
        return Probability(result.numerator, result.denominator)
    
    def __str__(self):
        return f"{self.prob} ({float(self.prob):.2%})"

# Roll a die
roll_six = Probability(1, 6)
print(f"P(6): {roll_six}")                    # → 1/6 (16.67%)

# Roll two dice, both 6
both_six = roll_six.and_independent(roll_six)
print(f"P(6 and 6): {both_six}")              # → 1/36 (2.78%)

# Draw a heart or diamond from deck
heart = Probability(13, 52)
diamond = Probability(13, 52)
red_card = heart.or_mutually_exclusive(diamond)
print(f"P(red): {red_card}")                  # → 1/2 (50.00%)
```

### Pattern 6: Fraction Sequence Generator
```python
from fractions import Fraction

def fibonacci_fractions(n):
    """Generate Fibonacci ratios (approach golden ratio)"""
    a, b = Fraction(1), Fraction(1)
    ratios = []
    
    for _ in range(n):
        a, b = b, a + b
        ratios.append(b / a)
    
    return ratios

# Golden ratio approximations
ratios = fibonacci_fractions(10)
for i, ratio in enumerate(ratios, 1):
    print(f"F({i+1})/F({i}) = {ratio} ≈ {float(ratio):.6f}")

# Convergence to φ (golden ratio) ≈ 1.618034

def harmonic_series(n):
    """Generate first n terms of harmonic series"""
    return [Fraction(1, i) for i in range(1, n + 1)]

series = harmonic_series(5)
print(f"Harmonic series: {series}")
print(f"Sum: {sum(series)}")                  # → 137/60
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: Float Precision Issues
```python
from fractions import Fraction
from decimal import Decimal

# WRONG - Float precision loss
frac = Fraction(0.1)
print(frac)                          # → 3602879701896397/36028797018963968 (ugly!)

# RIGHT - Use string or Decimal
frac1 = Fraction('0.1')
print(frac1)                         # → 1/10 (clean!)

frac2 = Fraction(Decimal('0.1'))
print(frac2)                         # → 1/10 (clean!)
```

### Error 2: Division by Zero
```python
from fractions import Fraction

# WRONG
try:
    frac = Fraction(1, 0)            # ZeroDivisionError
except ZeroDivisionError:
    print("Cannot create fraction with zero denominator")

# WRONG
try:
    result = Fraction(1, 2) / Fraction(0, 1)  # ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")

# RIGHT - Check before creating
def safe_fraction(num, den):
    if den == 0:
        raise ValueError("Denominator cannot be zero")
    return Fraction(num, den)
```

### Error 3: Type Mixing
```python
from fractions import Fraction

# Mixed arithmetic returns float (usually undesired)
result = Fraction(1, 2) + 0.5        # → 1.0 (float!)

# RIGHT - Keep everything as Fraction
result = Fraction(1, 2) + Fraction(1, 2)  # → 1 (Fraction)

# OR - Convert at the end
fracs = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
total = sum(fracs, Fraction(0))
print(total)                         # → 1 (exact)
print(float(total))                  # → 1.0 (when needed)
```

### Error 4: Comparing with Tolerance
```python
from fractions import Fraction

# WRONG - Fractions are exact, no need for tolerance
frac1 = Fraction(1, 3)
frac2 = Fraction(2, 6)
# if abs(frac1 - frac2) < 0.0001:  # Unnecessary!

# RIGHT - Direct comparison
if frac1 == frac2:
    print("Equal")                   # → Equal (both are 1/3)

# Tolerance only needed when comparing to floats
frac = Fraction(1, 3)
float_val = 1 / 3
if abs(float(frac) - float_val) < 1e-10:
    print("Approximately equal")
```

### Error 5: Large Denominators
```python
from fractions import Fraction

# WRONG - Creating huge denominators
pi = 3.141592653589793
frac = Fraction(pi)
print(frac)                          # → Very large denominator!

# RIGHT - Use limit_denominator()
frac = Fraction(pi).limit_denominator(1000)
print(frac)                          # → 355/113 (readable)
print(float(frac))                   # → 3.1415929... (close enough)
```

---

## PERFORMANCE TIPS

1. **Use Decimal for input, not float**
   ```python
   from fractions import Fraction
   from decimal import Decimal
   
   # SLOW and imprecise
   Fraction(0.1)                     # Large denominator
   
   # FAST and precise
   Fraction(Decimal('0.1'))          # → 1/10
   Fraction('0.1')                   # → 1/10
   ```

2. **Limit denominator size for approximations**
   ```python
   # SLOW - huge numbers
   import math
   pi_exact = Fraction(math.pi)
   
   # FAST - controlled size
   pi_approx = Fraction(math.pi).limit_denominator(100)
   ```

3. **Avoid unnecessary conversions**
   ```python
   # SLOW - converts back and forth
   result = float(Fraction(1, 2)) + float(Fraction(1, 3))
   
   # FAST - stay in Fraction
   result = Fraction(1, 2) + Fraction(1, 3)
   final = float(result)             # Convert once at end
   ```

4. **Use integer operations when possible**
   ```python
   # SLOWER
   Fraction(100, 1) / Fraction(10, 1)
   
   # FASTER (but Fraction for exactness)
   100 // 10                         # Use int if appropriate
   ```

5. **Reuse Fraction objects**
   ```python
   # SLOW - recreates fractions
   for i in range(1000):
       result = Fraction(1, 2) + Fraction(1, 3)
   
   # FAST - reuse
   half = Fraction(1, 2)
   third = Fraction(1, 3)
   for i in range(1000):
       result = half + third
   ```

6. **Batch operations**
   ```python
   # SLOWER
   result = Fraction(0)
   for val in values:
       result = result + Fraction(val)
   
   # FASTER
   result = sum((Fraction(v) for v in values), Fraction(0))
   ```

---

## INTEGRATION WITH OTHER MODULES

### With `math` module
```python
from fractions import Fraction
import math

frac = Fraction(9, 4)

# Math functions work with Fractions
print(math.sqrt(float(frac)))        # → 1.5
print(math.floor(frac))              # → 2
print(math.ceil(frac))               # → 3
print(math.trunc(frac))              # → 2

# GCD and LCM
print(math.gcd(12, 18))              # → 6
print(math.lcm(12, 18))              # → 36 (Python 3.9+)
```

### With `statistics` module
```python
from fractions import Fraction
from statistics import mean, median, stdev

data = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)]

print(mean(data))                    # → 13/36 (exact mean)
print(median(data))                  # → 1/3 (exact median)
# print(stdev(data))                 # Returns float
```

### With `numpy` (caution)
```python
from fractions import Fraction
import numpy as np

# NumPy converts Fractions to float
arr = np.array([Fraction(1, 2), Fraction(1, 3)])
print(arr)                           # → [0.5  0.33333333]
print(arr.dtype)                     # → float64

# Use object dtype to preserve Fractions (slower)
arr = np.array([Fraction(1, 2), Fraction(1, 3)], dtype=object)
print(arr)                           # → [Fraction(1, 2) Fraction(1, 3)]
```

---

## WHEN TO USE FRACTIONS

### ✅ Use Fractions When:
- **Exact arithmetic is required** (financial calculations, scientific measurements)
- **Working with ratios** (music theory, aspect ratios, recipes)
- **Avoiding floating-point errors** (0.1 + 0.2 ≠ 0.3)
- **Educational purposes** (teaching math concepts)
- **Small denominators** (most practical fractions)

### ❌ Don't Use Fractions When:
- **Performance is critical** (Fractions are slower than floats)
- **Working with irrational numbers** (π, e, √2 - use floats)
- **Large-scale numerical computing** (use NumPy with floats)
- **Interfacing with C libraries** (usually expect floats)
- **Denominators grow very large** (defeats the purpose)

---

## SUMMARY CHEAT SHEET

```python
from fractions import Fraction
from decimal import Decimal

# Creation
Fraction(3, 4)                       # From integers
Fraction('0.75')                     # From string (best for decimals)
Fraction(Decimal('0.75'))            # From Decimal (exact)
Fraction(0.75)                       # From float (may be imprecise)

# Properties
.numerator                           # Get numerator
.denominator                         # Get denominator

# Arithmetic
frac1 + frac2                        # Addition
frac1 * frac2                        # Multiplication
frac1 / frac2                        # Division

# Conversion
float(frac)                          # To float
int(frac)                            # To int (truncate)
str(frac)                            # To string "n/d"

# Approximation
.limit_denominator(max_d)            # Simplify to small denominator

# Common patterns
sum(fractions, Fraction(0))          # Sum list of fractions
Fraction(pi).limit_denominator(100)  # Approximate float
```

---

## REFERENCES & RESOURCES

- **Official Documentation**: https://docs.python.org/3/library/fractions.html
- **PEP 3141**: A Type Hierarchy for Numbers
- **Related Modules**: `decimal`, `numbers`, `math`
- **Use Cases**: Finance, music theory, ratios, exact arithmetic
