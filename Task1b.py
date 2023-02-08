#scores dicitonary : used instead of list as we can use key value pairs
with open ("scores.txt", "r") as f:
    scores = []
    for line in f:
        line = line.strip().split(' ')
        line[1] = int(line[1])
        scores.append(line)
scores_dict = dict(scores)

#list of the tiles
with open ("tiles.txt", "r") as f:
    tiles = []
    for line in f:
        line = line.strip()
        tiles.append(line)

#list of the word dictionary:
with open ("dictionary.txt", "r") as f:
    dictionary = []
    for line in f:
        line = line.strip()
        dictionary.append(line)
