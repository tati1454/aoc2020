import re

dbEntries = []

class PasswordEntry():
    def __init__(self, contain, atLeast, atMost, password):
        self.contain = contain
        self.atLeast = atLeast
        self.atMost = atMost
        self.password = password

def readFile():
    with open("input.txt", "r") as f:
        for line in f:
            entry = parseLine(line)
            dbEntries.append(entry)

def parseLine(line):
    match = re.search(r"^([0-9]*)", line)
    atLeast = int(match[0])
    
    match = re.search(r"-([0-9]*)", line)
    atMost = int(match[0].replace('-', ''))

    match = re.search(r"\s\S", line)
    contain = match[0].replace(' ', '')

    password = line.split(":")[1]
    password = password.replace(' ', '')

    return PasswordEntry(contain, atLeast, atMost, password)


def solution():
    correctPasswordsCounter = 0

    for entry in dbEntries:
        ocurrences = entry.password.count(entry.contain)
        if ocurrences < entry.atLeast or ocurrences > entry.atMost:
            continue

        correctPasswordsCounter += 1

    print(correctPasswordsCounter)

if __name__ == "__main__":
    readFile()
    solution()