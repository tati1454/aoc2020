puzzleInput = []

with open("input.txt", "r") as f:
    for line in f:
        line.replace('\n', '')
        line = int(line)

        puzzleInput.append(line)

def solution():
    for n1 in puzzleInput:
        for n2 in puzzleInput:
            if (n1 + n2) == 2020:
                print(n1 * n2)

if __name__ == "__main__":
    solution()
