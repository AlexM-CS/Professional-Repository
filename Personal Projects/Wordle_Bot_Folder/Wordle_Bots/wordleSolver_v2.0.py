# Alexander Myska          2-15-2024
# Wordle-bot is a Wordle-solving algorithm I have created entirely on my own
# This is Version 2.0, a more intelligent algorithm that uses additional logic to
# get the most information possible out of each guess, arriving at an answer faster.
# The most impactful part of this algorithm is the bonus system. Words are given bonuses to their score
# when they contain no duplicate letters, encouraging the algorithm to select words that are more unique
# and will gather more information. Words are also given bonuses when they contain special sequences, such as "QU" or "CH."

# UPDATES FROM 1.1:
# (1) New function "addBonus()": will add to a given word's score depending on whether it meets certain criteria
# This function helps the bot make better individual word choices
# (2) New function "multiplyBonus()": will mulitply a given word's score depending on whether it meets certain criteria
# This function will mainly be used to discourage the bot from choosing words that contain duplicate letters

# -------------------------------------------------
# STEP 1 - Import Words and place them in a list
# -------------------------------------------------

def getWordList(): # Creates a list object that stores every available word
    wordFile = open("acceptableWords.txt", "r")

    words = wordFile.readline()
    words = words.split(" ")
    # print(words) # Use this line for debugging only

    return words

# -------------------------------------------------
# STEP 2 - Define functions that speak to the user
# -------------------------------------------------

def greeting(): # Greets the user
    print()
    print("## Hello user. This is Wordle Solver version 2.0. Let's get solving! ##")

def reportScores(bestWord): # Reports which word performed the best
    print("## After some thought, I think the best word to guess would be: ##")
    print("## {0}. It had the highest score in the list of words still allowed, with a score of {1}. ##".format(bestWord[0], bestWord[1]))

def congratulations():
    print("## Congrats on finding the right word! See you later! ##")
    print()
    quit()

def failed():
    print("## Looks like we didn't get the word this time. Better luck next time! ##")
    print()
    quit()

# -------------------------------------------------
# STEP 3 - Define functions that collect user input
# -------------------------------------------------

def wait(): # Creates an intermediate line to separate large blocks of text and give the user a chance to read
    input("Press ENTER to continue...")
    print()

def makeGuess(wordList):
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

def checkForDuplicates(guess): # Checks to see if a given word has duplicate letters or not. If it does, returns True
    letter1 = guess[0]
    letter2 = guess[1]
    letter3 = guess[2]
    letter4 = guess[3]
    letter5 = guess[4]

    if (letter1 == letter2) or (letter1 == letter3) or (letter1 == letter4) or (letter1 == letter5):
        return letter1
    if (letter2 == letter3) or (letter2 == letter4) or (letter2 == letter5):
        return letter2
    if (letter3 == letter4) or (letter3 == letter5):
        return letter3
    if (letter4 == letter5):
        return letter4
    
def addBonus(word): # Gives a word bonus points for meeting certain criteria

    extraScore = 0
    numVowels = 0

    vowels = ["A","E","I","O","U"]

    for i in range(0, len(vowels)): # This code block reduces a word's score exponentially the more vowels it has
        if (vowels[i] in word):
            numVowels += 1
    extraScore -= (numVowels ** 1.45)

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

    if (duplicates != None):
        multiplier = 0.8

    return multiplier

def findBestWord(wordList): # Calculates a "score" for every word in the provided list and then selects the word with the highest score

    frequency = {}
    frequency["A"] = 8.12
    frequency["B"] = 1.49
    frequency["C"] = 2.71
    frequency["D"] = 4.32
    frequency["E"] = 12.02
    frequency["F"] = 2.30
    frequency["G"] = 2.03
    frequency["H"] = 5.92
    frequency["I"] = 7.31
    frequency["J"] = 0.10
    frequency["K"] = 0.69
    frequency["L"] = 3.98
    frequency["M"] = 2.61
    frequency["N"] = 6.95
    frequency["O"] = 7.68
    frequency["P"] = 1.82
    frequency["Q"] = 0.11
    frequency["R"] = 6.02
    frequency["S"] = 6.28
    frequency["T"] = 9.10
    frequency["U"] = 2.88
    frequency["V"] = 1.11
    frequency["W"] = 2.09
    frequency["X"] = 0.17
    frequency["Y"] = 2.11
    frequency["Z"] = 0.07

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

        if (letter not in wordList[i][position - 1]):
            newList.append(wordList[i])
            
    return newList

# Function to be used to "Correct"
def letterInPosition(letter, position, wordList): # Creates a new list only containing words with the given letter in the given position
    # NOTE - "position" is 1-5, NOT the index of the letter
    newList = []

    for i in range(0, len(wordList)):

        if (letter in wordList[i][position - 1]):
            newList.append(wordList[i])

    return newList

# Function to be used for "Close"
def letterInWrongPosition(letter, position, wordList): # Creates a new list only containing words with the given letter, but NOT in the given position
    # NOTE - "position" is 1-5, NOT the index of the letter
    newList = []

    for i in range(0, len(wordList)):

        if (letter in wordList[i]) and (wordList[i][position - 1] != letter):
            newList.append(wordList[i])

    return newList

def editList(guess, slot1Results, slot2Results, slot3Results, slot4Results, slot5Results, wordList): # Changes the list according to the results of the previous guess

    duplicates = checkForDuplicates(guess)

    if (slot1Results == "Correct"):
        wordList = letterInPosition(guess[0], 1, wordList)
    elif (slot1Results == "Close"):
        wordList = letterInWrongPosition(guess[0], 1, wordList)
    elif (slot1Results == "Incorrect"):         
        if (duplicates == guess[0]):
            wordList = letterNotInPosition(duplicates, 1, wordList)
        else:
            wordList = noWordsWith(guess[0], wordList)

    if (slot2Results == "Correct"):
        wordList = letterInPosition(guess[1], 2, wordList)
    elif (slot2Results == "Close"):
        wordList = letterInWrongPosition(guess[1], 2, wordList)
    elif (slot2Results == "Incorrect"):
        duplicates = checkForDuplicates(guess)
         
        if (duplicates == guess[1]):
            wordList = letterNotInPosition(duplicates, 2, wordList)
        else:
            wordList = noWordsWith(guess[1], wordList)


    if (slot3Results == "Correct"):
        wordList = letterInPosition(guess[2], 3, wordList)
    
    elif (slot3Results == "Close"):
        wordList = letterInWrongPosition(guess[2], 3, wordList)

    elif (slot3Results == "Incorrect"):
        duplicates = checkForDuplicates(guess)
         
        if (duplicates == guess[2]):
            wordList = letterNotInPosition(duplicates, 3, wordList)
        else:
            wordList = noWordsWith(guess[2], wordList)


    if (slot4Results == "Correct"):
        wordList = letterInPosition(guess[3], 4, wordList)
    
    elif (slot4Results == "Close"):
        wordList = letterInWrongPosition(guess[3], 4, wordList)

    elif (slot4Results == "Incorrect"):
        duplicates = checkForDuplicates(guess)
         
        if (duplicates == guess[3]):
            wordList = letterNotInPosition(duplicates, 4, wordList)
        else:
            wordList = noWordsWith(guess[3], wordList)

    
    if (slot5Results == "Correct"):
        wordList = letterInPosition(guess[4], 5, wordList)
    
    elif (slot5Results == "Close"):
        wordList = letterInWrongPosition(guess[4], 5, wordList)

    elif (slot5Results == "Incorrect"):
        duplicates = checkForDuplicates(guess)
         
        if (duplicates == guess[4]):
            wordList = letterNotInPosition(duplicates, 5, wordList)
        else:
            wordList = noWordsWith(guess[4], wordList)

    return wordList

# -------------------------------------------------
# STEP 6 - Put it all together
# -------------------------------------------------

def main():
    wordList = getWordList()
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