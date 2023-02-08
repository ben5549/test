import Task1b
keys = list(Task1b.scores_dict.keys()) #this gets us the letters os the alphabet from the scores dicitonary we made earlier

def onlyEnglishLetters(aWord:str):
    aWord = aWord.upper()
    check = True
    for i in aWord:
        if i not in keys:
            check = False
            break
    return (check)
    
print(onlyEnglishLetters("Hello"))
print(onlyEnglishLetters("He llo"))
print(onlyEnglishLetters("He3llo"))