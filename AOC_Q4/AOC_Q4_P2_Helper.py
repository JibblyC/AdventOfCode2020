import re

def check_byr(inputString):
    intValue = int(inputString)
    return intValue >= 1920 and intValue <=2002

def check_iyr(inputString):
    intValue = int(inputString)
    return intValue >= 2010 and intValue <=2020

def check_eyr(inputString):
    intValue = int(inputString)
    return intValue >= 2020 and intValue <=2030

def check_hgt(inputString):
    if "cm" in inputString:
        intValue = int(inputString[0:len(inputString) - 2])
        return intValue >= 150 and intValue <= 193
    elif "in" in inputString:
        intValue = int(inputString[0:len(inputString) - 2])
        return intValue >= 59 and intValue <= 76
    else:
        return False
    
def check_hcl(inputString):
    if "#" in inputString:
        pattern = '[0-9 a-fA-F]{6}'
        stringNoHash = inputString[1:]
        if len(stringNoHash) == 6:
            result = re.match(pattern,stringNoHash)
            if result:
                return True
    return False
    

def check_ecl(inputString):
    eyeColorArray = ["amb","blu","brn","gry","grn","hzl","oth",]
    for currentEyeColor in eyeColorArray:
        if currentEyeColor in inputString:
            return True
    return False

def check_pid(inputString):
    if len(inputString) == 9:
        pattern = '[0-9]{6}'
        result = re.match(pattern,inputString)
        if result:
            return True
    return False

def extract_vredential_value(credential,lineToCheckCreds):
    lineToCheckCreds = lineToCheckCreds.rstrip()
    placeHolder = lineToCheckCreds.split(credential + ":",1)
    return placeHolder[1].split(" ",1)[0]

def check_credential_is_valid(credential,lineToCheckCreds):
    value = extract_vredential_value(credential,lineToCheckCreds)
    if credential == "byr":
        return check_byr(value)
    if credential == "iyr":
        return check_iyr(value)
    if credential == "eyr":
        return check_eyr(value)
    if credential == "hgt":
        return check_hgt(value)
    if credential == "hcl":
        return check_hcl(value)
    if credential == "ecl":
        return check_ecl(value)
    if credential == "pid":
        return check_pid(value)  