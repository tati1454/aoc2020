import threading

threeMap = []

def readFile():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            threeMap.append(line * (len(lines)))

def calculateSlope(right, down):
    countOfTrees = 0

    x = 0
    y = 0
    while True:
        y += down
        x += right
        try:
            char = threeMap[y][x]
            if(char == "#"):
                countOfTrees += 1
        except IndexError:
            break

    return countOfTrees

def solution():
    r1 = calculateSlope(1, 1)
    r2 = calculateSlope(3, 1)
    r3 = calculateSlope(5, 1)
    r4 = calculateSlope(7, 1)
    r5 = calculateSlope(1, 2)
    
    print(r1 * r2 * r3 * r4 * r5)

readFile()
solution()