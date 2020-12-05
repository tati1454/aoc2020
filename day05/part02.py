seatLocations = []

def readFile():
    with open("input.txt", "r") as f:
        global seatLocations
        seatLocations = f.readlines()

def searchRow(location):
    min = 0
    max = 127

    for position in location:
        if position == "F":
            max = (max + min) // 2

        elif position == "B":
            min = ((max + min) // 2) + 1

        if min == max:
            return min

def searchColumn(location):
    min = 0
    max = 7

    for position in location:
        if position == "L":
            max = (max + min) // 2
        
        elif position == "R":
            min = ((max + min) // 2) + 1

        if min == max:
            return min

def getIds():
    IDs = []

    for location in seatLocations:
        rowLocation = location[:8]
        columnLocation = location[7:]

        row = searchRow(rowLocation)
        column = searchColumn(columnLocation)
        id = (row * 8) + column
        IDs.append(id)

    return IDs

def solution():
    IDs = getIds()
    IDs.sort()

    for i in range(0, len(IDs) - 1):
        if(i == 0):
            continue
        
        if not ((IDs[i] - IDs[i - 1]) == 1):
            print("SOLUTION: " + str(IDs[i - 1]))
            break

if __name__ == "__main__":
    readFile()
    solution()
    