# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
#writing to a text file
print("Creating a text file with the write() method.")
text_file = open("write_it1.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close()


#Reading the newly created file.
print("\nReading the newly created file.")
text_file = open("write_it1.txt", "r")
print(text_file.read())
text_file.close()


#Creating a text file with the writelines()
print("\nCreating a text file with the writelines() method.")
text_file = open("write_it2.txt", "w")
lines = ["Line 10\n",
         "This is line 20\n",
         "That makes this line 30\n"]
text_file.writelines(lines)
text_file.close()

#Reading the newly created file.
print("\nReading the newly created file.")
text_file = open("write_it2.txt", "r")
print(text_file.read())
text_file.close()

#writing directly
f = open('somefile.txt', 'w')
f.write('Hello, ')
f.write('World!')
f.close()

#Reading the newly created file.
print("\nReading the newly created file.")
text_file = open("somefile.txt", "r")
print(text_file.read())
text_file.close()
