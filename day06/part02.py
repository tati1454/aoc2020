import re

groupsAnswers = []

def readFile():
    with open("input.txt", "r") as f:
        buf = []
        for line in f:
            if line == "\n":
                groupsAnswers.append(buf)
                buf = []
                continue

            buf.append(line.replace('\n', ''))

        groupsAnswers.append(buf)

def solution():
    count = 0

    for group in groupsAnswers:
        answersCount = getAnswersCount(group)
        
        for v in answersCount.values():
            if v == len(group):
                count += 1

    print(count)

def getAnswersCount(group):
    answersCount = {}
    
    for answer in group:
        for char in answer:
            if char in answersCount:
                answersCount[char] += 1
                continue
            
            answersCount[char] = 1
    
    return answersCount

if __name__ == "__main__":
    readFile()
    solution()
    