input_array = []
rightMovement = [1,3,5,7,1]
moveDownTwoCheck = 0
arrayOfTreesCounted = []
skiplineCheck = 0


with open("AOC_Q3/Q3_input.txt") as my_file:
    input_array = my_file.readlines()


for currentRightMovement in rightMovement:
    countOfTrees = 0
    rightMovementCalculation = 0
    for currentLine in input_array:
        if len(arrayOfTreesCounted) == 4 and rightMovementCalculation != 0:
            skiplineCheck += 1
        if skiplineCheck % 2 == 0:
            currentLine = currentLine.rstrip()
            if(rightMovementCalculation != 0):
                if len(currentLine) <= rightMovementCalculation :
                    while len(currentLine) <= rightMovementCalculation:
                        currentLine += currentLine
                if(currentLine[rightMovementCalculation] == "#") :
                    countOfTrees += 1
            rightMovementCalculation += currentRightMovement
    arrayOfTreesCounted.append(countOfTrees)


partOneAnswer = arrayOfTreesCounted[1]
partTwoAnswer = 1

for count in arrayOfTreesCounted:
    partTwoAnswer *= count

print("Answer to Part One: {}".format(partOneAnswer))
print("Answer to Part Two: {}".format(partTwoAnswer))





