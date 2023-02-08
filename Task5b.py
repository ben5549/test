import Task1b, Task2b, Task3b, Task4b

def canBeMade(aWord, myTiles):
    try:
        aWord = aWord.upper()
        check = True
        checkTiles = myTiles.copy() 
        #we use the copy check tiles, to avoid modifiyng the original tiles list, which will be required for TASK7
        for i in aWord:
            if i not in checkTiles:
                check = False
                break
            checkTiles.remove(i)
        if check:
            return ("Can Be Made")
        else:
            return ("Can Not Be Made")
    except:
        return(False)



tiles = ['T','Y','S','E','U','W','I']
print(canBeMade("SWEET",tiles))
tiles = ['A','B','A','C','I','N','A','T','I','O','N','E']
print(canBeMade("ABACINATE",tiles))