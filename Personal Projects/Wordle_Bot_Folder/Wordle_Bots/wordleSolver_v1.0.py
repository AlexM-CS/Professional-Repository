# Alexander Myska          2-9-2024
# Wordle-bot is a Wordle-solving algorithm I have created entirely on my own
# This is Version 1.0, a low-level bot that makes suggestion based entirely on letter frequency
# and what slots are still unoccupied. While not a good strategy, this is likely enough to get most
# wordles solved within the six allowed guesses.

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
    print("## Hello user. This is Wordle Solver version 1.0. Let's get solving! ##")
    print()

def reportScores(bestWord): # Reports which word performed the best
    print("## After some thought, I think the best word to guess would be: ##")
    print("## {0}. It had the highest score in the list of words still allowed, with a score of {1}. ##".format(bestWord[0], bestWord[1]))

def congratulations():
    print("## Congrats on finding the right word! See you later! ##")
    return False

# -------------------------------------------------
# STEP 3 - Define functions that collect user input
# -------------------------------------------------

def wait(): # Creates an intermediate line to separate large blocks of text and give the user a chance to read
    input("Press ENTER to continue...")
    print()

def makeGuess():
    print("## Please tell me what word you will guess. Please use all capital letters. ##")
    print()
    guess = input("Your guess will be: ")
    return guess

def getWordPerformance(guess): # Gets user input on the previous word's performance

    print("## Please tell me how the word '{0}' did. ##".format(guess))
    print("## To tell me, type 'Correct', 'Close', 'Incorrect,' or 'Finished.' ##")
    wait()

    print("## Use 'Correct' when the letter and position are correct. ##")
    print("## Use 'Close' when the letter is correct but the position is not. ##")
    print("## Use 'Incorrect' when neither the letter nor position are correct. ##")
    print("## Use 'Finished' when we have correctly guessed te entire word.")
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

# TODO - Function that collets input on whether the guess was correct
    
# -------------------------------------------------
# STEP 4 - Define functions that find the optimal word
# -------------------------------------------------
    
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

        if (score > currentBest[1]):
            currentBest = [wordList[i], score]

    return currentBest
    # print(currentBest) # Use for debugging
            
# -------------------------------------------------
# STEP 5 - Define functions that edit the list of words being used
# -------------------------------------------------

# Function to be used for "Incorrect"
def letterNotInPosition(letter, position, wordList): # Creates a new list containing words without the given letter and words that do not contain the letter in the given position
    newList = []

    for i in range(0, len(wordList)):

        if (letter not in wordList[i]) or (wordList[i][position - 1] != letter):
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

    if (slot1Results == "Correct"):
        wordList = letterInPosition(guess[0], 1, wordList)
    
    elif (slot1Results == "Close"):
        wordList = letterInWrongPosition(guess[0], 1, wordList)

    elif (slot1Results == "Incorrect"):
         wordList = letterNotInPosition(guess[0], 1, wordList)


    if (slot2Results == "Correct"):
        wordList = letterInPosition(guess[1], 2, wordList)
    
    elif (slot2Results == "Close"):
        wordList = letterInWrongPosition(guess[1], 2, wordList)

    elif (slot2Results == "Incorrect"):
        wordList = letterNotInPosition(guess[1], 2, wordList)


    if (slot3Results == "Correct"):
        wordList = letterInPosition(guess[2], 3, wordList)
    
    elif (slot3Results == "Close"):
        wordList = letterInWrongPosition(guess[2], 3, wordList)

    elif (slot3Results == "Incorrect"):
        wordList = letterNotInPosition(guess[2], 3, wordList)


    if (slot4Results == "Correct"):
        wordList = letterInPosition(guess[3], 4, wordList)
    
    elif (slot4Results == "Close"):
        wordList = letterInWrongPosition(guess[3], 4, wordList)

    elif (slot4Results == "Incorrect"):
        wordList = letterNotInPosition(guess[3], 4, wordList)

    
    if (slot5Results == "Correct"):
        wordList = letterInPosition(guess[4], 5, wordList)
    
    elif (slot5Results == "Close"):
        wordList = letterInWrongPosition(guess[4], 5, wordList)

    elif (slot5Results == "Incorrect"):
        wordList = letterNotInPosition(guess[4], 5, wordList)

    return wordList

# -------------------------------------------------
# STEP 6 - Put it all together
# -------------------------------------------------

def main():
    wordList = getWordList()
    greeting()
    wait()

    running = True

    while (running):
        
        bestWord = findBestWord(wordList)
        reportScores(bestWord)
        wait()

        guess = makeGuess()
        wait()

        slot1Results, slot2Results, slot3Results, slot4Results, slot5Results = getWordPerformance(guess)

        if (slot1Results == "Finished"):
            running = congratulations()
        
        else:
            wordList = editList(guess, slot1Results, slot2Results, slot3Results, slot4Results, slot5Results, wordList)

if __name__ == "__main__":
    main()