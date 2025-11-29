# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
#read a file with name and grades
# splits the line into 2 fields based on space

files = open('studentinfo.txt','r')
lenFirst = 10
lenLast = 10


while 1:
    lastName = files.read(lenFirst)

    position = files.seek(0,1)
    firstName = files.read(lenLast)
    position = files.seek(0,1)
    grade = files.readline()

    if len(lastName) == 0:
        break
    print('The Last Name read is -> ', len(firstName))
    print('The First Name read is -> ', lastName)
    print('The Grade is -> ', grade)

files.close()
