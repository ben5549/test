import Task1b, Task2b

def getLetterScore(aLetter):
    try:
        check = False
        aLetter = aLetter.upper()
        for key, value in Task1.scores_dict.items():
            if key == aLetter:
                check = True
                return (value)
    except:
        print(0)
        print("Make sure have entered a single alphabet and as a string")
