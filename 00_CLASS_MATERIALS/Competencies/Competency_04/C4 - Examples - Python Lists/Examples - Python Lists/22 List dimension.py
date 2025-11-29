# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 8, 5;
Matrix = [[0 for x in range(w)] for y in range(h)]
Matrix[0][0] = 1
#Matrix[6][0] = 3 # error! range... 
Matrix[0][6] = 3 # valid

print (Matrix[0][0]) # prints 1
x, y = 0, 6 
print (Matrix[x][y]) # prints 3; be careful with indexing!

for i in range(len(Matrix)):
    for j in range(len(Matrix[i])):
        print(Matrix[i][j], end=' ')
    print()
