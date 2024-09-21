words = open("wordleAcceptable.txt", "r")
newFile = open("wordleAcceptableConverted.txt","w")

line = words.read()

# print(line) # For debugging purposes

newFile.write(line.upper())