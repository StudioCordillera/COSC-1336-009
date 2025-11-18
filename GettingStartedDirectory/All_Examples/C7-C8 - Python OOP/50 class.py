
def Greatest():
    inFile = open('Anything.txt','r')
    line = inFile.readline()
    highNum = line
    
    while line:
        if line > highNum:
            highNum = line
        line = inFile.readline()
    inFlie.close()
    return highNum
Greatest()
        
