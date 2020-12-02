import re

dbEntries = []

class PasswordEntry():
    def __init__(self, contain, firstPosition, secondPosition, password):
        self.contain = contain
        self.firstPosition = firstPosition
        self.secondPosition = secondPosition
        self.password = password

def readFile():
    with open("input.txt", "r") as f:
        for line in f:
            entry = parseLine(line)
            dbEntries.append(entry)

def parseLine(line):
    match = re.search(r"^([0-9]*)", line)
    firstPosition = int(match[0])
    
    match = re.search(r"-([0-9]*)", line)
    secondPosition = int(match[0].replace('-', ''))

    match = re.search(r"\s\S", line)
    contain = match[0].replace(' ', '')

    password = line.split(":")[1]
    password = password.replace(' ', '')

    return PasswordEntry(contain, firstPosition, secondPosition, password)

def solution():
    correctPasswordsCounter = 0

    for entry in dbEntries:
        firstCharacter = entry.password[entry.firstPosition - 1]
        secondCharacter = entry.password[entry.secondPosition - 1]

        if firstCharacter == entry.contain and secondCharacter == entry.contain:
            continue

        if firstCharacter == entry.contain or secondCharacter == entry.contain:
            correctPasswordsCounter += 1


    print(correctPasswordsCounter)

if __name__ == "__main__":
    readFile()
    solution()