words = open("wordleArchive.txt", "r")
newFile = open("wordleArchiveConverted.txt","w")

line = words.readline()
line = line.split(" ")

# print(line) # For debugging purposes

for i in range(0, len(line)):
    newFile.write("{0}\n".format(line[i]))