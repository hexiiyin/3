aList = []

while True:
        num = input()
        if num != "":
            aList.append(num)
        else:
            break

aList = list(map(int,aList))

def sortings(n):
    nList = []
    zList = []
    pList = []

    for i in aList:
        if i < 0:
            nList.append(i)
        
        elif i == 0:
            zList.append(i)

        elif i > 0:
            pList.append(i)

sortings(aList)