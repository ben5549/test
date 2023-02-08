Tiles = []
Scores = dict()
Dictionary = []

with open("tiles.txt","r") as f:
    for line in f:
        line = line.strip()
        Tiles.append(line)


with open("scores.txt","r") as f:
    for line in f:
        line = line.strip()
        line = line.split()
        n = 0
        n1 = 1
        Scores.update({line[n]:line[n1]})
        n = n+1
        n1 = n1 + 1

with open("dictionary.txt","r") as f:
    for line in f:
        line = line.split()
        Dictionary.append(line)




