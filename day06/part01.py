import re

groupsAnswers = []

def readFile():
    with open("input.txt", "r") as f:
        buf = ""
        for line in f:
            if line == "\n":
                groupsAnswers.append(buf)
                buf = ""
                continue

            buf += line

def solution():
    count = 0
    for answers in groupsAnswers:
        answeredYes = []

        for char in answers:
            if re.match(r"[a-z]", char) != None and char not in answeredYes:
                answeredYes.append(char)

        count += len(answeredYes)
        print(answeredYes)

    print(count)

readFile()
solution()
