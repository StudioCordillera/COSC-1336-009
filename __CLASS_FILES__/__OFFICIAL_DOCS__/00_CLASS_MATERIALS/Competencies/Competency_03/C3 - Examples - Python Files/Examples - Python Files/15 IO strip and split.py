# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
files = open('studentgrades.txt','r')

for line in files:
    line = line.rstrip('\n')
    if len(line) > 0:
        lineSplit = line.split(" ")
        print('The line read -> ', line)
        print('\t' + 'The first field -> ', lineSplit[0])
        print('\t' + 'The first field -> ', lineSplit[1])
files.close()
