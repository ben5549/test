import Task1b, Task2b, Task3b, Task4b, Task5b
        
def isValid(aWord, myTiles, aDictionary):
    aWord = aWord.upper()
    if not Task2b.onlyEnglishLetters(aWord):
        return "Not a valid word"
    elif aWord not in aDictionary:
        return "Word not in dictionary"
    elif Task5b.canBeMade(aWord, myTiles) != "Can Be Made":
        return "Word can't be made from the tiles"
    return (f"'{aWord}' has a score of: {Task4b.getWordScore(aWord)}")



tiles = ['T','Y','S','E','E','W','I']
print(isValid("sweet",tiles, Task1b.dictionary))