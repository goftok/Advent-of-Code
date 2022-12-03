source = r"/Users/Helloworld/Desktop/Advent-of-Code/Day_2/input.txt"

with open(source) as f:
    s1 = 0
    s2 = 0
    points1 = {
        "A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 0,
        "C Y": 2 + 6,
        "C Z": 3 + 3,
    }
    points2 = {
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6,
    }
    for line in f.read().splitlines():
        s1 += points1[line]
        s2 += points2[line]
    #Part one
    print(s1)
    #Part two
    print(s2)
