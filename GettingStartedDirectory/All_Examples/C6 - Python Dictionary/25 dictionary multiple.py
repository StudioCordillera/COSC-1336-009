# Name      Ally Baba
# Date      February 7 2020
# Program   dictionary
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# The dict() constructor builds dictionaries directly from sequences of key-value pairs:

tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(tel)
print(tel['sape'])
print(list(tel.keys()))
print('guido' in tel)

# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

tel = {x: x**2 for x in (2, 4, 6)}
print(tel)

#When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

tel = dict(sape=4139, guido=4127, jack=4098)
print(tel)



