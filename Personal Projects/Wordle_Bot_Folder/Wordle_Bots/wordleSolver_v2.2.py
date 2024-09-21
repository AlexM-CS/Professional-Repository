# Alexander Myska          2-19-2024
# Wordle-bot is a Wordle-solving algorithm I have created entirely on my own
# This is Version 2.2, a more intelligent algorithm that uses additional logic to
# get the most information possible out of each guess, arriving at an answer faster.
# The most impactful part of this algorithm is the bonus system. Words are given bonuses to their score
# when they contain no duplicate letters, encouraging the algorithm to select words that are more unique
# and will gather more information. Words are also given bonuses when they contain special sequences, such as "QU" or "CH."

# UPDATES FROM 2.1:
# (1) The function "checkForDuplicates()": used to only find the first duplicate letter present in a word.
# For example, the word "CACAO" features a duplicate letter C and a duplicate letter A,
# but the function returns before it finds the duplicate letter A. This would cause a chain reaction
# eventually leading to an error. For example, if the first A is correct but the second is incorrect,
# Then every word without an A in slot 2 would be romved, and then every word with an A would be removed.
# To fix this issue, the function now iterates through the entire word, and returns a list of all the duplicates it finds
# instead of simply returning the first duplicate it finds
# (2) To facilitate this new version of checkForDuplicates(), multiple changes also needed to be made to multiplyBonus()
# Now, it checks for the length of the list returned, and applies a multiplier accordingly.
# While there are currently no words in the database that are five letters long and contain only 2 unique letters
# (i.e., the list of duplicates would be longer than 2), this functionality was implemented for future use.

# Various UI Updates:
# (1) Added descriptions for every function program-side

# -------------------------------------------------
# STEP 1 - Import Words and place them in a list
# -------------------------------------------------

def getWordList(fileName, mode): # Creates a list object that stores every available word
    wordFile = open("Wordle_Bot_Folder/Wordle_Resources/" + fileName, mode)

    words = wordFile.readline()
    words = words.split(" ")
    # print(words) # Use this line for debugging only

    return words

# -------------------------------------------------
# STEP 2 - Define functions that speak to the user
# -------------------------------------------------

def greeting(): # Greets the user
    print()
    print("## Hello user. This is Wordle Solver version 2.2. Let's get solving! ##")

def reportScores(bestWord): # Reports which word performed the best
    print("## After some thought, I think the best word to guess would be: ##")
    print("## {0}. It had the highest score in the list of words still allowed, with a score of {1}. ##".format(bestWord[0], bestWord[1]))

def congratulations(): # Called when the game is won
    print("## Congrats on finding the right word! See you later! ##")
    print()
    quit()

def failed(): # Called when the game is lost
    print("## Looks like we didn't get the word this time. Better luck next time! ##")
    print()
    quit()

# -------------------------------------------------
# STEP 3 - Define functions that collect user input
# -------------------------------------------------

def wait(): # Creates an intermediate line to separate large blocks of text and give the user a chance to read
    input("Press ENTER to continue...")
    print()

def makeGuess(wordList): # Prompts the user to enter their guess that will be used for the algorithm's calculations
    print("## Please tell me what word you will guess. Please use all capital letters. ##")
    print()
    guess = input("Your guess will be: ")

    while (guess not in wordList):
        print("Sorry, that was not a valid input.")
        print()
        guess = input("Your guess will be: ")

    return guess

def getWordPerformance(guess, attemptNumber): # Gets user input on the previous word's performance

    if (attemptNumber == 1):

        print("## Please tell me how the word '{0}' did. ##".format(guess))
        print("## To tell me, type 'Correct', 'Close', 'Incorrect,' or 'Finished.' ##")
        wait()

        print("## Use 'Correct' when the letter and position are correct. ##")
        print("## Use 'Close' when the letter is correct but the position is not. ##")
        print("## Use 'Incorrect' when neither the letter nor position are correct. ##")
        print("## Use 'Finished' when we have correctly guessed the entire word.")
        wait()

    slot1 = input("## What was the state of slot 1? ## ")
    while (slot1 != "Correct") and (slot1 != "Close") and (slot1 != "Incorrect") and (slot1 != "Finished"):
        print("Sorry, that was not a valid input.")
        print()
        slot1 = input("## What was the state of slot 1? ## ")

    if (slot1 == "Finished"):
        return "Finished", "Finished", "Finished", "Finished", "Finished"

    slot2 = input("## What was the state of slot 2? ## ")
    while (slot2 != "Correct") and (slot2 != "Close") and (slot2 != "Incorrect") and (slot2 != "Finished"):
        print("Sorry, that was not a valid input.")
        print()
        slot2 = input("## What was the state of slot 2? ## ")

    if (slot2 == "Finished"):
        return "Finished", "Finished", "Finished", "Finished", "Finished"
    
    slot3 = input("## What was the state of slot 3? ## ")
    while (slot3 != "Correct") and (slot3 != "Close") and (slot3 != "Incorrect") and (slot3 != "Finished"):
        print("Sorry, that was not a valid input.")
        print()
        slot3 = input("## What was the state of slot 3? ## ")

    if (slot3 == "Finished"):
        return "Finished", "Finished", "Finished", "Finished", "Finished"

    slot4 = input("## What was the state of slot 4? ## ")
    while (slot4 != "Correct") and (slot4 != "Close") and (slot4 != "Incorrect") and (slot4 != "Finished"):
        print("Sorry, that was not a valid input.")
        print()
        slot4 = input("## What was the state of slot 4? ## ")

    if (slot4 == "Finished"):
        return "Finished", "Finished", "Finished", "Finished", "Finished"

    slot5 = input("## What was the state of slot 5? ## ")
    while (slot5 != "Correct") and (slot5 != "Close") and (slot5 != "Incorrect") and (slot5 != "Finished"):
        print("Sorry, that was not a valid input.")
        print()
        slot5 = input("## What was the state of slot 5? ## ")

    if (slot5 == "Finished"):
        return "Finished", "Finished", "Finished", "Finished", "Finished"

    print()
    print("## Thank you for your feedback. Calculating...")
    wait()
    
    return slot1, slot2, slot3, slot4, slot5
    
# -------------------------------------------------
# STEP 4 - Define functions that find the optimal word
# -------------------------------------------------

def checkForDuplicates(guess): # Checks to see if a given word has duplicate letters or not. If it does, returns the letter(s) found

    duplicateList = []

    letter1 = guess[0]
    letter2 = guess[1]
    letter3 = guess[2]
    letter4 = guess[3]
    letter5 = guess[4]

    if (letter1 == letter2) or (letter1 == letter3) or (letter1 == letter4) or (letter1 == letter5):
        duplicateList.append(letter1)
    if (letter2 == letter3) or (letter2 == letter4) or (letter2 == letter5):
        duplicateList.append(letter2)
    if (letter3 == letter4) or (letter3 == letter5):
        duplicateList.append(letter3)
    if (letter4 == letter5):
        duplicateList.append(letter4)

    return duplicateList
    
def addBonus(word): # Gives a word bonus points for meeting certain criteria

    extraScore = 0
    numVowels = 0

    vowels = ["A","E","I","O","U"]

    for i in range(0, len(vowels)): # This code block reduces a word's score exponentially the more vowels it has
        for j in range(0, len(word)):
            if vowels[i] == word[j]:
                numVowels += 1

    extraScore -= (numVowels ** 1.3)

    # Consonant clusters

    # Low-level clusters
    l_clusters = ["BL","BR","CL","CR","DR","FL","FR","GL","GR","PL","PR","SH","SL","ST","TR"]

    for i in range(0, len(l_clusters)): # These blocks give bonus points for words with consonant clusters
        if (l_clusters[i] in word):
            extraScore += 0.5

    # High-level clusters
    h_clusters = ["QU","CH","TH"]

    for i in range(0, len(h_clusters)): # This encourages the bot to make more varied guesses that can yield more information
        if (h_clusters[i] in word):
            extraScore += 1.5

    return extraScore

def multiplyBonus(word): # This function will give words multipliers depending on if they meet certain criteria

    multiplier = 1
    duplicates = checkForDuplicates(word)

    if (len(duplicates) == 1):
        multiplier = 0.8
    elif (len(duplicates) == 2):
        multiplier = 0.6
    elif (len(duplicates) > 2):
        multiplier = 0.4

    return multiplier

def createFrequencyDict(wordList): # Creates a frequency database for the word list being used
    
    numLetterA = 0
    numLetterB = 0
    numLetterC = 0
    numLetterD = 0
    numLetterE = 0
    numLetterF = 0
    numLetterG = 0
    numLetterH = 0
    numLetterI = 0
    numLetterJ = 0
    numLetterK = 0
    numLetterL = 0
    numLetterM = 0
    numLetterN = 0
    numLetterO = 0
    numLetterP = 0
    numLetterQ = 0
    numLetterR = 0
    numLetterS = 0
    numLetterT = 0
    numLetterU = 0
    numLetterV = 0
    numLetterW = 0
    numLetterX = 0
    numLetterY = 0
    numLetterZ = 0

    totalLetters = 0

    for i in range(0, len(wordList)):
        
        word = wordList[i]

        for j in range (0, len(word)):

            letter = word[j]

            totalLetters += 1
            if (letter == "A"): numLetterA += 1
            elif (letter == "B"): numLetterB += 1
            elif (letter == "C"): numLetterC += 1
            elif (letter == "D"): numLetterD += 1
            elif (letter == "E"): numLetterE += 1
            elif (letter == "F"): numLetterF += 1
            elif (letter == "G"): numLetterG += 1
            elif (letter == "H"): numLetterH += 1
            elif (letter == "I"): numLetterI += 1
            elif (letter == "J"): numLetterJ += 1
            elif (letter == "K"): numLetterK += 1
            elif (letter == "L"): numLetterL += 1
            elif (letter == "M"): numLetterM += 1
            elif (letter == "N"): numLetterN += 1
            elif (letter == "O"): numLetterO += 1
            elif (letter == "P"): numLetterP += 1
            elif (letter == "Q"): numLetterQ += 1
            elif (letter == "R"): numLetterR += 1
            elif (letter == "S"): numLetterS += 1
            elif (letter == "T"): numLetterT += 1
            elif (letter == "U"): numLetterU += 1
            elif (letter == "V"): numLetterV += 1
            elif (letter == "W"): numLetterW += 1
            elif (letter == "X"): numLetterX += 1
            elif (letter == "Y"): numLetterY += 1
            else: numLetterZ += 1

    frequency = {}

    frequency["A"] = round(((numLetterA / totalLetters) * 100), 2)
    frequency["B"] = round(((numLetterB / totalLetters) * 100), 2)
    frequency["C"] = round(((numLetterC / totalLetters) * 100), 2)
    frequency["D"] = round(((numLetterD / totalLetters) * 100), 2)
    frequency["E"] = round(((numLetterE / totalLetters) * 100), 2)
    frequency["F"] = round(((numLetterF / totalLetters) * 100), 2)
    frequency["G"] = round(((numLetterG / totalLetters) * 100), 2)
    frequency["H"] = round(((numLetterH / totalLetters) * 100), 2)
    frequency["I"] = round(((numLetterI / totalLetters) * 100), 2)
    frequency["J"] = round(((numLetterJ / totalLetters) * 100), 2)
    frequency["K"] = round(((numLetterK / totalLetters) * 100), 2)
    frequency["L"] = round(((numLetterL / totalLetters) * 100), 2)
    frequency["M"] = round(((numLetterM / totalLetters) * 100), 2)
    frequency["N"] = round(((numLetterN / totalLetters) * 100), 2)
    frequency["O"] = round(((numLetterO / totalLetters) * 100), 2)
    frequency["P"] = round(((numLetterP / totalLetters) * 100), 2)
    frequency["Q"] = round(((numLetterQ / totalLetters) * 100), 2)
    frequency["R"] = round(((numLetterR / totalLetters) * 100), 2)
    frequency["S"] = round(((numLetterS / totalLetters) * 100), 2)
    frequency["T"] = round(((numLetterT / totalLetters) * 100), 2)
    frequency["U"] = round(((numLetterU / totalLetters) * 100), 2)
    frequency["V"] = round(((numLetterV / totalLetters) * 100), 2)
    frequency["W"] = round(((numLetterW / totalLetters) * 100), 2)
    frequency["X"] = round(((numLetterX / totalLetters) * 100), 2)
    frequency["Y"] = round(((numLetterY / totalLetters) * 100), 2)
    frequency["Z"] = round(((numLetterZ / totalLetters) * 100), 2)

    return frequency

def findBestWord(wordList): # Calculates a "score" for every word in the provided list and then selects the word with the highest score

    frequency = createFrequencyDict(wordList)
    # print(frequency) # Use this for debugging

    currentBest = ["XXXXX", 0.00]

    for i in range(0,len(wordList)):

        score = 0 # Initial score for every word

        slot1 = wordList[i][0] # First letter
        slot2 = wordList[i][1] # Second letter
        slot3 = wordList[i][2] # Third letter
        slot4 = wordList[i][3] # Fourth letter
        slot5 = wordList[i][4] # Fifth letter

        keys = frequency.keys()

        for entry in keys:
            if (slot1 == entry):
                score += frequency[entry]
            if (slot2 == entry):
                score += frequency[entry]
            if (slot3 == entry):
                score += frequency[entry]
            if (slot4 == entry):
                score += frequency[entry]
            if (slot5 == entry):
                score += frequency[entry]

        score = (score + addBonus(wordList[i])) * multiplyBonus(wordList[i])

        if (score > currentBest[1]):
            currentBest = [wordList[i], round(score, 2)]

    return currentBest
            
# -------------------------------------------------
# STEP 5 - Define functions that edit the list of words being used
# -------------------------------------------------

# Function to be used for "Incorrect" when there are NO duplicate letters
def noWordsWith(letter, wordList): # Creates a new list containing only words without the give letter
    newList = []

    for i in range(0, len(wordList)):

        if (letter not in wordList[i]):
            newList.append(wordList[i])

    return newList

# Function to be used for "Incorrect" when there are duplicate letters
def letterNotInPosition(letter, position, wordList): # Creates a new list containing only words with the given letter NOT in the given position
    newList = []

    for i in range(0, len(wordList)):

        if (letter not in wordList[i][position]):
            newList.append(wordList[i])
            
    return newList

# Function to be used to "Correct"
def letterInPosition(letter, position, wordList): # Creates a new list only containing words with the given letter in the given position
    newList = []

    for i in range(0, len(wordList)):

        if (letter in wordList[i][position]):
            newList.append(wordList[i])

    return newList

# Function to be used for "Close"
def letterInWrongPosition(letter, position, wordList): # Creates a new list only containing words with the given letter, but NOT in the given position
    newList = []

    for i in range(0, len(wordList)):

        if (letter in wordList[i]) and (wordList[i][position] != letter):
            newList.append(wordList[i])

    return newList

def editList(guess, slot1Results, slot2Results, slot3Results, slot4Results, slot5Results, wordList): # Changes the list according to the results of the previous guess

    duplicates = checkForDuplicates(guess)

    if (slot1Results == "Correct"):
        wordList = letterInPosition(guess[0], 0, wordList)
    elif (slot1Results == "Close"):
        wordList = letterInWrongPosition(guess[0], 0, wordList)
    elif (slot1Results == "Incorrect"):         
        if (guess[0] in duplicates):
            wordList = letterNotInPosition(guess[0], 0, wordList)
        else:
            wordList = noWordsWith(guess[0], wordList)

    if (slot2Results == "Correct"):
        wordList = letterInPosition(guess[1], 1, wordList)
    elif (slot2Results == "Close"):
        wordList = letterInWrongPosition(guess[1], 1, wordList)
    elif (slot2Results == "Incorrect"):         
        if (guess[1] in duplicates):
            wordList = letterNotInPosition(guess[1], 1, wordList)
        else:
            wordList = noWordsWith(guess[1], wordList)


    if (slot3Results == "Correct"):
        wordList = letterInPosition(guess[2], 2, wordList)
    elif (slot3Results == "Close"):
        wordList = letterInWrongPosition(guess[2], 2, wordList)
    elif (slot3Results == "Incorrect"):         
        if (guess[2] in duplicates):
            wordList = letterNotInPosition(guess[2], 2, wordList)
        else:
            wordList = noWordsWith(guess[2], wordList)


    if (slot4Results == "Correct"):
        wordList = letterInPosition(guess[3], 3, wordList)
    elif (slot4Results == "Close"):
        wordList = letterInWrongPosition(guess[3], 3, wordList)
    elif (slot4Results == "Incorrect"):   
        if (guess[3] in duplicates):
            wordList = letterNotInPosition(guess[3], 3, wordList)
        else:
            wordList = noWordsWith(guess[3], wordList)

    if (slot5Results == "Correct"):
        wordList = letterInPosition(guess[4], 4, wordList)
    elif (slot5Results == "Close"):
        wordList = letterInWrongPosition(guess[4], 4, wordList)
    elif (slot5Results == "Incorrect"):         
        if (guess[4] in duplicates):
            wordList = letterNotInPosition(guess[4], 4, wordList)
        else:
            wordList = noWordsWith(guess[4], wordList)

    return wordList

# -------------------------------------------------
# STEP 6 - Put it all together
# -------------------------------------------------

def main(): # Function that runs the bot
    wordList = getWordList("acceptableWords.txt", "r")
    greeting()
    wait()

    attemptNumber = 1
    running = True

    while (running):
        
        bestWord = findBestWord(wordList)

        if (bestWord[0] == "XXXXX"):
            failed()

        reportScores(bestWord)
        wait()

        guess = makeGuess(wordList)
        wait()

        slot1Results, slot2Results, slot3Results, slot4Results, slot5Results = getWordPerformance(guess, attemptNumber)

        if (slot1Results == "Finished"):
            congratulations()
        else:
            wordList = editList(guess, slot1Results, slot2Results, slot3Results, slot4Results, slot5Results, wordList)

        if (attemptNumber > 5):
            failed()
        
        attemptNumber += 1

if __name__ == "__main__":
    main()