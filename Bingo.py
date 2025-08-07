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
                if bingoCard[key][i] >= 10:
                    print(str(bingoCard[key][i]) + " ",end="")

                else:
                    print(str(bingoCard[key][i]) + "  ",end="")

            else:
                print(str(bingoCard[key][i]))

createCard()
outputCard()