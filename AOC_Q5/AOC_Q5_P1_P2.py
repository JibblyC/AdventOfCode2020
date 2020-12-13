import array

input_array = []

rows = list(range(128))
columns = list(range(8))

seatIDArray = []

    
with open("AOC_Q5/Q5_input.txt") as my_file:
    input_array = my_file.readlines()

for line in input_array:
    line = line.rstrip()
    rowCheckArray = rows.copy()
    columnCheckArray = columns.copy()   
    for charToCheck in line:
        if charToCheck == "L":
            indexToCheck = int(len(columnCheckArray) / 2)
            columnCheckArray = columnCheckArray[:indexToCheck]
        if charToCheck == "R":
            indexToCheck = int((len(columnCheckArray) / 2) * -1)
            columnCheckArray = columnCheckArray[indexToCheck:]
        if charToCheck == "F":
            indexToCheck = int(len(rowCheckArray) / 2)
            rowCheckArray = rowCheckArray[:indexToCheck]
        if charToCheck == "B":
            indexToCheck = int((len(rowCheckArray) / 2) * -1)
            rowCheckArray = rowCheckArray[indexToCheck:]
    seatIDValue = (rowCheckArray[0] * 8) + columnCheckArray[0]
    seatIDArray.append(seatIDValue)



print("Highest Seat ID is : {} ".format(max(seatIDArray)))

seatIDArray.sort()
for seat in seatIDArray:
    indexInArray = seatIDArray.index(seat)
    if indexInArray + 1 < len(seatIDArray):
        if seatIDArray[indexInArray + 1] - seat == 2:
            print("Your Seat number is : {}".format(seat + 1))
        


