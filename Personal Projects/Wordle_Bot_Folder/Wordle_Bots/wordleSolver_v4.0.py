# Alexander Myska          5-8-2024
# Wordle-bot is a Wordle-solving algorithm I have created entirely on my own
# This is Version 4.0, a version of the bot that searches for the best guesses to gather information.
# To do this, it creates a list of all the possible words after the first guess, and then searches for other letters
# in the following guesses to try to collect more information.
# In short, it stores the value of any correct letters and doesn't use them until it is down to a small number of possible answers.

# To accomplish this, I rewrote the program with this new, information-first mindset

# UPDATES FROM 3.2:
# (1) Uses a more intelligent, information-first algorithm to reduce the number of average guesses.
# (2) Is now capable of accessing files from different folders.
# (3) Re-wrote various parts to be more time/memory efficient, such as the creation of the frequency dictionary.

import random

# -------------------------------------------------
# STEP 1 - Import Words and place them in a list
# -------------------------------------------------

def getWordList(fileName, mode): # Creates a list object that stores every available word

    if (fileName != "Default"):
        wordFile = open("Wordle_Bot_Folder/Wordle_Resources/" + fileName, mode)
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

def getArchiveList(): # Creates an alternate list to compare against
    wordFile = open("Wordle_Bot_Folder/Wordle_Resources/wordleArchive.txt","r")

    words = wordFile.readline()
    altList = words.split(" ")

    wordFile.close()

    for i in range(0, len(altList)):
        if (len(altList[i]) != 5):
            altList.remove(altList[i])

    return altList

def getAnswerList(): # Creates an alternate list to compare against
    wordFile = open("Wordle_Bot_Folder/Wordle_Resources/wordleAcceptable.txt","r")

    words = wordFile.readline()
    altList = words.split(" ")

    wordFile.close()

    for i in range(0, len(altList)):
        if (len(altList[i]) != 5):
            altList.remove(altList[i])

    return altList

def getScrabbleList(): # Creates an alternate list to compare against
    wordFile = open("Wordle_Bot_Folder/Wordle_Resources/scrabbleDictionary.txt","r")

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
    print("## Hello user. This is Wordle Solver version 4.0. Let's get solving! ##")

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
    
    try:
        getWordList(fileName, "r")
    except:
        print("## Sorry, I couldn't find that file anywhere. ##")
        print()
        quit()

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

def checkForDuplicates(guess):
    duplicates = list()

    letter0 = guess[0]
    letter1 = guess[1]
    letter2 = guess[2]
    letter3 = guess[3]
    letter4 = guess[4]
    
    if (letter0 == letter1 or letter0 == letter2 or letter0 == letter3 or letter0 == letter4):
        duplicates.append(letter0)
    if (letter1 == letter2 or letter1 == letter3 or letter1 == letter4):
        duplicates.append(letter1)
    if (letter2 == letter3 or letter2 == letter4):
        duplicates.append(letter2)
    if (letter3 == letter4):
        duplicates.append(letter3)

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
            if word[j] in frequency:
                frequency[word[j]] += 1
            else:
                frequency[word[j]] = 1
            totalLetters += 1
            
    for key in frequency:
        frequency[key] = round(((frequency[key] / totalLetters) * 100), 2)

    return frequency

def findBestGuess(attemptNumber, lastGuess, wordList, otherList1, otherList2, otherList3):

    if (attemptNumber == 2): # Second guess- use all different letters, get more information
        
        editedList = wordList.copy() # This code block only allows us to use words without the previous guess's letters
        for i in range(0, len(lastGuess)):
            editedList = noWordsWith(lastGuess[i], editedList)
        
        frequency = createFrequencyDict(editedList)

        currentBest = ["XXXXX", 0.00]

        for i in range(0,len(editedList)):

            slot1 = editedList[i][0] # First letter
            slot2 = editedList[i][1] # Second letter
            slot3 = editedList[i][2] # Third letter
            slot4 = editedList[i][3] # Fourth letter
            slot5 = editedList[i][4] # Fifth letter
            
            score = frequency[slot1] + frequency[slot2] + frequency[slot3] + frequency[slot4] + frequency[slot5]

            score = (score + addBonus(editedList[i])) * multiplyBonus(editedList[i], otherList1, otherList2, otherList3)

            if (score > currentBest[1]):
                currentBest = [editedList[i], round(score, 2)]

        return currentBest    

    else: # Search for the optimal word
        frequency = createFrequencyDict(wordList)

        currentBest = ["XXXXX", 0.00]

        for i in range(0,len(wordList)):

            slot1 = wordList[i][0] # First letter
            slot2 = wordList[i][1] # Second letter
            slot3 = wordList[i][2] # Third letter
            slot4 = wordList[i][3] # Fourth letter
            slot5 = wordList[i][4] # Fifth letter

            score = frequency[slot1] + frequency[slot2] + frequency[slot3] + frequency[slot4] + frequency[slot5]

            score = (score + addBonus(wordList[i])) * multiplyBonus(wordList[i], otherList1, otherList2, otherList3)

            if (score > currentBest[1]):
                currentBest = [wordList[i], round(score, 2)]

        return currentBest

# -------------------------------------------------
# STEP 5 - Define functions that edit the list of words being used
# -------------------------------------------------

# Function to be used for "Incorrect" when there are NO duplicate letters
def noWordsWith(letter, wordList): # Creates a new list containing only words without the given letter
    newList = []

    for i in range(0, len(wordList)):

        if (letter not in wordList[i]):
            newList.append(wordList[i])

    return newList

def noWordsWithout(letter, wordList): # Creates a new list containing only words with the given letter
    newList = []

    for i in range(0, len(wordList)):

        if (letter in wordList[i]):
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

# Functions to be used for "Close"
def letterInWrongPosition(letter, position, wordList): # Creates a new list only containing words with the given letter, but NOT in the given position
    newList = []

    for i in range(0, len(wordList)):

        if (letter in wordList[i]) and (wordList[i][position] != letter):
            newList.append(wordList[i])

    newList = noWordsWithout(letter, newList)

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
    database = getDatabase()
    wordList = getWordList(database, "r")

    otherList1 = getArchiveList()
    otherList2 = getAnswerList()
    otherList3 = getScrabbleList()

    if (wordList == otherList1):
        otherList1 = []
    elif (wordList == otherList2):
        otherList2 = []
    elif (wordList == otherList3):
        otherList3 = []

    greeting()
    wait()

    attemptNumber = 1
    lastGuess = "     "
    running = True

    while (running):
        
        bestWord = findBestGuess(attemptNumber, lastGuess, wordList, otherList1, otherList2, otherList3)
        
        if (bestWord[0] == "XXXXX"):
            failed()

        reportScores(bestWord)
        wait()

        guess = makeGuess(wordList)
        lastGuess = guess
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