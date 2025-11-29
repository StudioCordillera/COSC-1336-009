# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# read a file char by character

file = open('test.txt','r')

while 1:
    char = file.read(1)
    if not char:
        break
    print('The character read is -> ', char)

file.close()

