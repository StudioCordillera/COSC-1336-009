# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
def number_convert(n):
    val = int(n)
    return val

file = open('test.txt', 'r')
numbers = file.readline()
print(numbers)

#Then split that string to a list so I can use each number block individually...
numbers = numbers.split()
print (numbers)

numeric_numbers = []
sum = 0

for x in numbers:
    y = number_convert(x)
    sum = sum + y
    numeric_numbers.append(y)

print (numeric_numbers)
print(sum)




