threeMap = []

def readFile():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            threeMap.append(line * (len(lines)))

def solution():
    countOfTrees = 0

    x = 0
    y = 0
    while True:
        y += 1
        x += 3
        try:
            char = threeMap[y][x]
            if(char == "#"):
                countOfTrees += 1
        except IndexError:
            break
    
    print(countOfTrees)

readFile()
solution()