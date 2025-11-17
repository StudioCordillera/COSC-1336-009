# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
files = open('student.txt','r')

for line in files:
    line = line.rstrip('\n')
    print(line)

files.close()
