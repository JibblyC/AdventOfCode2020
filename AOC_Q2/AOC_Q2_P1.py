input_array = []
countCorrect = 0


with open("AOC_Q2/Q2_input.txt") as my_file:
    input_array = my_file.readlines()

for currentString in input_array:

    splitStringArray =  currentString.split(' ', 1)
    leftSide = splitStringArray[0]
    rightSide = splitStringArray[1]

    minDigit = int(leftSide.split('-')[0])
    maxDigit = int(leftSide.split('-')[1])

    charToCheck = rightSide[0]

    splitRightSideArray = rightSide.split(':')
    stringToCheck =  splitRightSideArray[1]

    countOfOccur = stringToCheck.count(charToCheck)

    if countOfOccur >=minDigit and countOfOccur <= maxDigit:
        countCorrect += 1

print("Correct Passwords count : {}".format(countCorrect))
