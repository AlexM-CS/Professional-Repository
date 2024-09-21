# Alexander Myska          6-27-2024
# Wordle-bot is a Wordle-solving algorithm I have created entirely on my own
# This is Version 5.0, a drastic improvement from the exploitable methods used by bot 4.0.
# Instead of starting with the same two guesses each time, it will keep track of letters
# that it has found as a part of the word and only refrain from guessing those (kind of).
# It will now keep track of this using a system that tells it when to switch from information-gathering mode
# to word-solving mode.
# This is a much more effective version of the information-first mindest I used in my last update,
# because it will continue to stay in search mode until it receives enough information to start
# thinking about the answer rather than just potential letters.

# UPDATES FROM 4.0:
# (1) Added two new lists- foundLetters and wrongLetters, that the program uses while it is still in
# information mode. It uses these lists so that it knows which letters it should ignore.
# These needed to be separated into two different lists because wrong letteres should never be guessed in any circumstance,
# but correct letters should be ignored only temporarily.
# (2) Fixed some messy code in various areas, improving the program's efficiency and speed.
# (3) New function "editHelper()": Allows for the editList() function to be condensed by
# reducing the amount of redundant code that needs to be written
# (4) Removed function "noWordsWithout()"
# (5) Removed the "lastGuess" variable(s) and functionality they had, which was replaced by the new found and wrong letter lists

import random    

# -------------------------------------------------
# STEP 1 - Import Words and place them in a list
# -------------------------------------------------

def getWordList(fileName): # Creates a list object that stores every available word
    
    try:
        if (fileName != "Default"):
            wordFile = open("Wordle_Bot_Folder/Wordle_Resources/" + fileName, "r")
        else:
            wordFile = open("Wordle_Bot_Folder/Wordle_Resources/scrabbleDictionary.txt", "r")

        words = wordFile.readline()
        wordList = words.split(" ")
        # print(words) # Use this line for debugging only

        wordFile.close()

        for i in range(0, len(wordList)): # This block is included to prevent errors later in the program
            if (len(wordList[i]) != 5):
                wordList.remove(wordList[i])

        return wordList
    
    except:
        print("## Sorry, I couldn't find that file anywhere. ##")
        print()
        quit()

def getArchiveList(): # Creates an alternate list to compare against
    wordFile = open("Wordle_Bot_Folder/Wordle_Resources/wordleArchive.txt","r") # list of answers from the archived version of wordle

    words = wordFile.readline()
    altList = words.split(" ")

    wordFile.close()

    for i in range(0, len(altList)):
        if (len(altList[i]) != 5):
            altList.remove(altList[i])

    return altList

def getAnswerList(): # Creates an alternate list to compare against
    wordFile = open("Wordle_Bot_Folder/Wordle_Resources/wordleAcceptable.txt","r") # list of allowed guesses

    words = wordFile.readline()
    altList = words.split(" ")

    wordFile.close()

    for i in range(0, len(altList)):
        if (len(altList[i]) != 5):
            altList.remove(altList[i])

    return altList

def getScrabbleList(): # Creates an alternate list to compare against
    wordFile = open("Wordle_Bot_Folder/Wordle_Resources/scrabbleDictionary.txt","r") # list of 5-letter words in the scrabble dictionary

    words = wordFile.readline()
    altList = words.split(" ")

    wordFile.close()

    for i in range(0, len(altList)):
        if (len(altList[i]) != 5):
            altList.remove(altList[i])

    return altList

# -------------------------------------------------
# STEP 2 - Define functions that speak to the user
# -------------------------------------------------

def greeting(): # Greets the user
    print()
    print("## Hello user. This is Wordle Solver version 5.0. Let's get solving! ##")

def reportScores(bestWord): # Reports which word performed the best
    dialogue = random.randrange(0, 3)

    if (dialogue == 0):
        print("## After some thought, I think the best word to guess would be: ##")
        print("## {0}. It had the highest score in the list of words still allowed, with a score of {1}. ##".format(bestWord[0], bestWord[1]))
    elif (dialogue == 1):
        print("## After running the numbers, the best word seems to be: ##")
        print("## {0}. It had the best score of the words still allowed, getting a {1}. ##".format(bestWord[0], bestWord[1]))
    else:
        print("## I Think the best word for us would be: ##")
        print("## {0}, which had the highest score in the list, scoring {1}. ##".format(bestWord[0], bestWord[1]))

def congratulations(): # Called when the game is won
    dialogue = random.randrange(0, 2)

    if (dialogue == 0):
        print("## Congrats on finding the right word! See you later! ##")
    else:
        print("## We did it! Let's solve some more again soon!")
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

def getDatabase():
    print("## First things first: what database should I work with? ##")
    print("## Please provide the EXACT file name of the database I should use below. ##")
    print()
    fileName = input("The file name of the database is: ")

    return fileName

def makeGuess(wordList): # Prompts the user to enter their guess that will be used for the algorithm's calculations
    print("## Please tell me what word you will guess, using all capital letters. ##")
    print()
    guess = input("Your guess will be: ").upper()

    while (len(guess) != 5):
        print("## Sorry, that was not a valid input. ##")
        print()
        guess = input("Your guess will be: ")

    return guess

def getWordPerformance(guess, attemptNumber): # Gets user input on the previous word's performance
        
    finished = "Finished", "Finished", "Finished", "Finished", "Finished"

    slot1 = input("## What was the state of slot 1? ## ")
    while (slot1 != "Correct") and (slot1 != "Close") and (slot1 != "Incorrect") and (slot1 != "Finished"):
        print("Sorry, that was not a valid input.")
        print()
        slot1 = input("## What was the state of slot 1? ## ")

    if (slot1 == "Finished"):
        return finished

    slot2 = input("## What was the state of slot 2? ## ")
    while (slot2 != "Correct") and (slot2 != "Close") and (slot2 != "Incorrect") and (slot2 != "Finished"):
        print("Sorry, that was not a valid input.")
        print()
        slot2 = input("## What was the state of slot 2? ## ")

    if (slot2 == "Finished"):
        return finished
    
    slot3 = input("## What was the state of slot 3? ## ")
    while (slot3 != "Correct") and (slot3 != "Close") and (slot3 != "Incorrect") and (slot3 != "Finished"):
        print("Sorry, that was not a valid input.")
        print()
        slot3 = input("## What was the state of slot 3? ## ")

    if (slot3 == "Finished"):
        return finished

    slot4 = input("## What was the state of slot 4? ## ")
    while (slot4 != "Correct") and (slot4 != "Close") and (slot4 != "Incorrect") and (slot4 != "Finished"):
        print("Sorry, that was not a valid input.")
        print()
        slot4 = input("## What was the state of slot 4? ## ")

    if (slot4 == "Finished"):
        return finished

    slot5 = input("## What was the state of slot 5? ## ")
    while (slot5 != "Correct") and (slot5 != "Close") and (slot5 != "Incorrect") and (slot5 != "Finished"):
        print("Sorry, that was not a valid input.")
        print()
        slot5 = input("## What was the state of slot 5? ## ")

    if (slot5 == "Finished"):
        return finished

    print()
    print("## Thank you for your feedback. Calculating...")
    wait()
    
    return slot1, slot2, slot3, slot4, slot5

# -------------------------------------------------
# STEP 4 - Define functions that find the optimal word
# -------------------------------------------------

def checkForDuplicates(guess):
    duplicates = list()
        
    for i in range(0, 5):
       j = 1
       while ((i + j) < 5):
           if (guess[i] == guess[i + j]):
               duplicates.append(guess[i])
               break
           j += 1

    return duplicates

def addBonus(word):
    extraScore = 0
    numVowels = 0

    vowels = ["A","E","I","O","U","Y"]

    for i in range(0, len(word)): # This code block reduces a word's score exponentially the more vowels it has
        if (word[i] in vowels):
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

def multiplyBonus(word, otherList1, otherList2, otherList3): # This function will give words multipliers depending on if they meet certain criteria

    multiplier = 1
    duplicates = checkForDuplicates(word)

    # Duplicate letters
    if (len(duplicates) == 1):
        multiplier -= 0.25
    elif (len(duplicates) == 2):
        multiplier -= 0.5
    elif (len(duplicates) > 2):
        multiplier -= 0.75

    # Word exists in multiple lists
    if (word in otherList1):
        multiplier += 0.15
    if (word in otherList2):
        multiplier += 0.25
    if (word in otherList3):
        multiplier += 0.1

    return multiplier

def createFrequencyDict(wordList): # Creates a frequency database for the word list being used
    
    frequency = dict()
    totalLetters = 0

    for i in range(0, len(wordList)):
        word = wordList[i]
        for j in range(0, len(word)):
            if (word[j] in frequency):
                frequency[word[j]] += 1
            else:
                frequency[word[j]] = 1
            totalLetters += 1
            
    for key in frequency:
        frequency[key] = round(((frequency[key] / totalLetters) * 100), 2)

    return frequency

def findBestGuess(attemptNumber, wordList, otherList1, otherList2, otherList3, foundLetters, wrongLetters, database):
    
    checkWords = wordList.copy()
    for i in range(0, len(foundLetters)):
        checkWords = noWordsWith(foundLetters[i], checkWords)
    for i in range(0, len(wrongLetters)):
        checkWords = noWordsWith(wrongLetters[i], checkWords)

    if (len(checkWords) - len(wordList) <= 100):
        checkWords = wordList

    frequency = createFrequencyDict(checkWords)

    currentBest = ["XXXXX", 0.00]

    for i in range(0,len(checkWords)):

        score = frequency[checkWords[i][0]] + frequency[checkWords[i][1]] + frequency[checkWords[i][2]] + frequency[checkWords[i][3]] + frequency[checkWords[i][4]]
        score = (score + addBonus(checkWords[i])) * multiplyBonus(checkWords[i], otherList1, otherList2, otherList3)

        if (score > currentBest[1]):
            currentBest = [checkWords[i], round(score, 2)]

    return currentBest

# -------------------------------------------------
# STEP 5 - Define functions that edit the list of words being used
# -------------------------------------------------

# Function to be used for "Incorrect" when there are NO duplicate letters
def noWordsWith(letter, wordList): # Creates a new list containing only words without the given letter
    newList = list()

    for i in range(0, len(wordList)):
        if (letter not in wordList[i]):
            newList.append(wordList[i])

    return newList

# Function to be used for "Incorrect" when there are duplicate letters
def letterNotInPosition(letter, position, wordList): # Creates a new list containing only words with the given letter NOT in the given position
    newList = list()

    for i in range(0, len(wordList)):
        if (letter not in wordList[i][position]):
            newList.append(wordList[i])
            
    return newList

# Function to be used to "Correct"
def letterInPosition(letter, position, wordList): # Creates a new list only containing words with the given letter in the given position
    newList = list()

    for i in range(0, len(wordList)):
        if (letter in wordList[i][position]):
            newList.append(wordList[i])

    return newList

# Functions to be used for "Close"
def letterInWrongPosition(letter, position, wordList): # Creates a new list only containing words with the given letter, but NOT in the given position
    newList = list()

    for i in range(0, len(wordList)):
        if (letter in wordList[i]) and (wordList[i][position] != letter):
            newList.append(wordList[i])

    return newList

def editList(guess, slot1Results, slot2Results, slot3Results, slot4Results, slot5Results, wordList, foundLetters, wrongLetters): # Changes the list according to the results of the previous guess

    duplicates = checkForDuplicates(guess)
    
    wordList, foundLetters, wrongLetters = editHelper(guess, duplicates, slot1Results, 0, wordList, foundLetters, wrongLetters)
    wordList, foundLetters, wrongLetters = editHelper(guess, duplicates, slot2Results, 1, wordList, foundLetters, wrongLetters)
    wordList, foundLetters, wrongLetters = editHelper(guess, duplicates, slot3Results, 2, wordList, foundLetters, wrongLetters)
    wordList, foundLetters, wrongLetters = editHelper(guess, duplicates, slot4Results, 3, wordList, foundLetters, wrongLetters)
    wordList, foundLetters, wrongLetters = editHelper(guess, duplicates, slot5Results, 4, wordList, foundLetters, wrongLetters)

    return wordList, foundLetters, wrongLetters

def editHelper(guess, duplicates, slotResult, slotNumber, wordList, foundLetters, wrongLetters): # Helper function to make above code cleaner
    
    if (slotResult == "Correct"):
        wordList = letterInPosition(guess[slotNumber], slotNumber, wordList)
        foundLetters.append(guess[slotNumber])
    elif (slotResult == "Close"):
        wordList = letterInWrongPosition(guess[slotNumber], slotNumber, wordList)
        foundLetters.append(guess[slotNumber])
    elif (slotResult == "Incorrect"):         
        if (guess[slotNumber] in duplicates):
            wordList = letterNotInPosition(guess[slotNumber], slotNumber, wordList)
        else:
            wordList = noWordsWith(guess[slotNumber], wordList)
            wrongLetters.append(guess[slotNumber])
    
    return wordList, foundLetters, wrongLetters

# -------------------------------------------------
# STEP 6 - Put it all together
# -------------------------------------------------

def main(): # Function that runs the bot
    database = getDatabase()
    wordList = getWordList(database)

    otherList1 = getArchiveList()
    otherList2 = getAnswerList()
    otherList3 = getScrabbleList()

    if (wordList == otherList1):
        otherList1 = list()
    elif (wordList == otherList2):
        otherList2 = list()
    elif (wordList == otherList3):
        otherList3 = list()

    greeting()
    wait()

    attemptNumber = 1
    foundLetters = list()
    wrongLetters = list()

    while True: # This loop will keep iterating until the Wordle is either solved or we fail
        bestWord = findBestGuess(attemptNumber, wordList, otherList1, otherList2, otherList3, foundLetters, wrongLetters, database)
        
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
            wordList, foundLetters, wrongLetters = editList(guess, slot1Results, slot2Results, slot3Results, slot4Results, slot5Results, wordList, foundLetters, wrongLetters)

        if (attemptNumber > 5):
            failed()
        
        attemptNumber += 1

if __name__ == "__main__":
    main()