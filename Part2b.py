import random as rd, Task1b, Task2b, Task3b, Task4b, Task5b, Task6b, Task7b
#this function requires you to enters the ditionary created in task1
def scrabble (aDictionary):
    #need to create a list of tiles chosen at random from the list of tiles in Task1
    gameTiles = []
    for i in range(1,8):
        copyTiles = Task1.tiles.copy()
        choice = rd.choice(copyTiles)
        Task1.tiles.remove(choice)
        gameTiles.append(choice)
    print(gameTiles)
    
    #now we prints the scores of the chose tiles.
    tileScores = []
    for item in gameTiles:
        tileScores.append([item, Task3.getLetterScore(item)])
    print(tileScores)
    
    while True:
        word = input("Please enter a word: ")
        word = word.upper()
        if word != "&&&":
            a = Task6.isValid(word,gameTiles,aDictionary)
            print(a)
            if a == (f"'{word}' has a score of: {Task4.getWordScore(word)}"):
                print ("well done, thanks for playing")
                break
        else:
            print("thankyou")
            return

scrabble(Task1.dictionary)