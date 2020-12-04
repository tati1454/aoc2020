import re

passports = []

def solution():
    validPassports = 0

    for passport in passports:
        if hasTheCorrectFields(passport) and validateFields(passport):
            validPassports += 1

    print(validPassports)


def hasTheCorrectFields(passport):
    return "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport \
        and "hcl" in passport and "ecl" in passport and "pid" in passport

def validateFields(passport):
    birthYear = passport['byr']
    issueYear = passport['iyr']
    expirationYear = passport['eyr']
    height = passport['hgt']
    hairColor = passport['hcl']
    eyeColor = passport['ecl']
    passportId = passport['pid']

    if (int(birthYear) >= 1920 and int(birthYear) <= 2002) and\
        (int(issueYear) >= 2010 and int(issueYear) <= 2020) and\
        (int(expirationYear) >= 2020 and int(expirationYear) <= 2030) and\
        (len(birthYear) == 4 and len(issueYear) == 4 and len(expirationYear) == 4) and\
        validateHeight(height) and\
        (re.match(r"#([0-9]|[a-f]){6}", hairColor) != None) and len(hairColor) == 7 and\
        (re.match(r"amb|blu|brn|gry|grn|hzl|oth", eyeColor) != None) and\
        (re.match(r"[0-9]{9}", passportId) != None) and len(passportId) == 9:
        
        return True
    
    else:
        return False

def validateHeight(height):
    if re.match(r"[0-9]*cm", height) != None:
        return int(height[:-2]) >= 150 and int(height[:-2]) <= 193
    
    elif re.match(r"[0-9]*in", height) != None:
        return int(height[:-2]) >= 59 and int(height[:-2]) <= 76
    
    else:
        return False

def readFile():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        rawPassports = splitPassports(lines)
        
        for rawPassport in rawPassports:
            passports.append(createDictionary(rawPassport))

def splitPassports(lines):
    passportsText = []

    passportText = ""

    for line in lines:
        if line == '\n':
            passportsText.append(passportText)
            passportText = ""
            continue
        
        passportText += line

    passportsText.append(passportText)
    return passportsText

def createDictionary(text):
    entries = re.split(r" |\n", text)
    dictionary = {}

    for entry in entries:
        if entry == '':
            continue

        keyValue = entry.split(':')
        key = keyValue[0]
        value = keyValue[1]

        dictionary[key] = value

    return dictionary

if __name__ == "__main__":
    readFile()
    solution()
    