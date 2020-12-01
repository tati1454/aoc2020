import itertools

puzzleInput = []

with open("input.txt", "r") as f:
    for line in f:
        line.replace('\n', '')
        line = int(line)

        puzzleInput.append(line)

def solution():
    iterator = itertools.combinations(puzzleInput, 3)

    for numbers in iterator:
        n1 = numbers[0]
        n2 = numbers[1]
        n3 = numbers[2]

        if (n1 + n2 + n3) == 2020:
            print(n1*n2*n3)

if __name__ == "__main__":
    solution()
