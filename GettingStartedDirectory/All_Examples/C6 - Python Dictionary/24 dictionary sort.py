# Name      Ally Baba
# Date      February 7 2020
# Program   dictionary
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

#print(tel['jack'])

del tel['sape']

tel['irv'] = 4127
# print(tel)

# print(list(tel.keys()))

print(sorted(tel.values()))

# print('guido' in tel)

print('jack' not in tel)



