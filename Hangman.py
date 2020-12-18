import random as r
from nltk.corpus import words
import os


hangmanStages = [
    """
     ______
    |      |
    |
    |
    |
    |
    |
----------
""",
    """
     ______
    |      |
    |      O
    |
    |
    |
    |
----------
""",
    """
     ______
    |      |
    |      O
    |     /|
    |
    |
    |
----------
""",
    """
     ______
    |      |
    |      O
    |     /|\\
    |
    |
    |
----------
""",
    """
     ______
    |      |
    |      O
    |     /|\\
    |      |
    |
    |
----------
""",
    """
     ______
    |      |
    |      O
    |     /|\\
    |      |
    |     /
    |
----------
""",
    """
     ______
    |      |
    |      O
    |     /|\\
    |      |
    |     / \\
    |
----------
"""
]
randWord = ""
wordHidden = []
wordRevealed = []

def pickMode(i):
    global randWord
    if i == 1:
        word_list = words.words()
        randWord = r.choice(word_list)
    elif i == 2:
        randWord = input("Please type the word: ")
    for i in range(len(randWord)):
        wordHidden.append("_")
        wordRevealed.append(randWord[i].upper())

def letterArrayCheck(letter,Array = []):
    try:
        Array.index(letter.upper())
        return True
    except:
        return False



def playGame():
    inp = input("Please select a mode to play:\n1) Against the machine\n2) 2-Player Mode\n")
    pickMode(inp)
    statusBool = None
    counter = 0
    pickLettersStr = ""
    pickLetters = []
    letterBool = False
    while True:
        stage = hangmanStages[counter]
        if statusBool == False:
            print("You made a wrong guess!")
        elif statusBool:
            print("You guessed right!")
        print(stage)
        for i in range(len(wordHidden)):
            print(wordHidden[i], end=" ")
        print("\nPicked letters: " + pickLettersStr, end="")
        letter = input("\nPlease guess a letter: ")
        letterBool = letterArrayCheck(letter, pickLetters)
        while letterBool:
            letter = input("You already picked that letter! Please pick another letter: ")
            letterBool = letterArrayCheck(letter, pickLetters)
        pickLettersStr += letter.upper() + ", "
        pickLetters.append(letter.upper())
        statusBool = guess(letter)
        if not statusBool:
            counter += 1
        if counter >= 6:
            print(chr(27) + "[2J")
            stage = hangmanStages[counter]
            print(stage)
            print("You lost the game! The word was: " + randWord.upper())
            break
        else:
            if not letterArrayCheck("_", wordHidden):
                print("You won!")
                break
        print(chr(27) + "[2J")


def guess(letter):
    counter = -1
    for i in range(len(wordRevealed)):
        if wordRevealed[i] == letter.upper():
            wordHidden[i] = wordRevealed[i]
            counter += 1
    if counter > -1:
        return True
    else:
        return False


playGame()