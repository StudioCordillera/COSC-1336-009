print("Creating a text file with the write() method.")
text_file = open("allybaba.txt", "w")
text_file.write("I love snoring 1\n")
text_file.close()


text_file = open("allybaba.txt", "r")
for lines in text_file:
    print(lines)
text_file.close()
