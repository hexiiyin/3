"""
A Bingo card consists of 5 columns of 5 numbers. 
The columns are labeled with the letters B, I, N, G and O. 
There are 15 numbers that can appear under each letter. 
In particular, the numbers that can appear under the B range from 1 to 15, 
the numbers that can appear under the I range from 16 to 30, the numbers 
that can appear under the N range from 31 to 45, and so on.

Write a function that creates a random Bingo card and stores it in a dictionary. 
The keys will be the letters B, I, N, G and O. The values will be the lists of 
five numbers that appear under each letter. Write a second function that displays 
the Bingo card with the columns labeled appropriately. Use these functions to write 
a program that displays a random Bingo card. Ensure that the main program only runs 
when the file containing your solution has not been imported into another program.
"""
import random

bingoCard = {}

def createCard():
    letterList = []
    bingo = ["B","I","N","G","O"]
    rangeOne = 1
    rangeTwo = 15

    for i in bingo:
        while len(letterList) != 5:
            num = random.randint(rangeOne,rangeTwo)
            if num not in letterList:
                letterList.append(num)

        bingoCard[i] = letterList
        letterList = []
        rangeOne = rangeTwo + 1
        rangeTwo += 15

    return bingoCard

def outputCard():
    for i in bingoCard:
        if i != "O":
            print(str(i) + "  ",end="")
        
        else:
            print(str(i))

    for i in range(5):
        for key in bingoCard:
            if key != "O":
                print(str(bingoCard[key][i]) + " ",end="")

            else:
                print(str(bingoCard[key][i]))

print(createCard())
outputCard()