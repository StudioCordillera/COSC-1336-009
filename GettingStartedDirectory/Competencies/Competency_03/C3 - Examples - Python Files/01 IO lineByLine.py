# Description
# read a file line by line

fileLine = open('test.txt','r')
# it opens a file in the current directory for READING
# assigns an OBJECT (Variable) to the opened file

for i in range(10):
         line = fileLine.readline()
                 #OBJECT - fileLine has a method called readline
         print('Loop Sequence ', str(i) + ': line in the file ->' + line)

fileLine.close()
          
