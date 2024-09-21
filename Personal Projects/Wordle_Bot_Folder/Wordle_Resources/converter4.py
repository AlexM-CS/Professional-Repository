words = open("wordleAcceptableConverted.txt", "r")
newFile = open("wordleAcceptable2.txt","w")

line = words.read()
line = line.split("\n")

for i in range(0, len(line)):
    newFile.write("{0} ".format(line[i]))