input_array = []
integer_array = []


with open("AOC_Q1/Q1_input.txt") as my_file:
    input_array = my_file.readlines()

for x in input_array:
    integer_array.append(int(x))

answer = 0

for x in integer_array:
    for y in integer_array:
        if x + y == 2020:
            answer = x * y
            break
    else:
        continue
    break

print("Answer 1 is {}".format(answer))

for x in integer_array:
    for y in integer_array:
        for z in integer_array:
            if x + y + z == 2020:
                answer = x * y * z
                break
        else:
            continue
    else:
        continue
    break

print("Answer 2 is {}".format(answer))
            
  