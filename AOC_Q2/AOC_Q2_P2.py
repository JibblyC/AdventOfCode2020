input_array = []
countCorrect = 0


with open("AOC_Q2/Q2_input.txt") as my_file:
    input_array = my_file.readlines()

for currentString in input_array:
    
    splitStringArray =  currentString.split(' ', 1)
    leftSide = splitStringArray[0]
    rightSide = splitStringArray[1]

    # No need to shift back 1 as there is a space in the split of the stringToCheck
    minDigitPosition = int(leftSide.split('-')[0])
    maxDigitPosition  = int(leftSide.split('-')[1])

    charToCheck = rightSide[0]

    splitRightSideArray = rightSide.split(':')
    stringToCheck =  splitRightSideArray[1]


    if stringToCheck[minDigitPosition] == charToCheck or stringToCheck[maxDigitPosition] == charToCheck:
        if(stringToCheck[minDigitPosition] != stringToCheck[maxDigitPosition]):
            countCorrect += 1


print("Correct Passwords count : {}".format(countCorrect))
