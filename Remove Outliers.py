def removeOut(n, l):
    if n * 2 > len(l):
        return "error"
    
    elif n * 2 <= len(l):
        modifiedList = l.copy()
        modifiedList.sort()
        
        for i in range(n):
            modifiedList.remove(max(modifiedList))
            modifiedList.remove(min(modifiedList))

        return modifiedList

firstNum = int(input())
secList = input().split()
secList = list(map(int,secList))

print(removeOut(firstNum, secList))
print(secList)