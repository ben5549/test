import  Task1b, Task2b, Task3b, Task4b, Task5b, Task6b

def highestWord (myTiles, aDictionary):
    #first we have create a list of all the words from the dicitonary that can be made from the tile given:
    possibleWords = []
    for word in aDictionary:
        if Task5b.canBeMade(word,myTiles) == "Can Be Made":
            possibleWords.append(word)
    #now we iterate over all the possible words, and use the getwordscore from Task 4, to create a list of scores for each word.
    scores = []
    for word in possibleWords:
        scores.append(Task4b.getWordScore(word))
    #now we find the index of the max number on the list of words:
    idx = scores.index(max(scores))
    #now we print the word matching that idx.
    print(f"The word with the highest score is: {possibleWords[idx]}. It's score is: {scores[idx]}")

tiles = ['A','B','A','C','I','N','A','T','I','O','N','E']
highestWord(tiles,Task1b.dictionary)