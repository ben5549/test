import Task1b, Task2b, Task3b

def getWordScore(aWord):
    try:
        score = 0
        for i in aWord:
            score += Task3b.getLetterScore(i)
        return score
    except:
        return(0)
    
print(getWordScore("SWEET"))