import string
input_array = []
values_to_check = list(string.ascii_lowercase)
current_section_array = []
number_of_yes_answers = []

with open("AOC_Q6/Q6_input.txt") as my_file:
    input_array = my_file.readlines()

for line in input_array:
    if line == "\n":
        currentSectionAsString = ''.join(current_section_array)
        yesCount = 0
        for currentCharacter in values_to_check:
            characterCount = currentSectionAsString.count(currentCharacter)
            if characterCount == len(current_section_array):
                yesCount += 1
        current_section_array.clear()
        number_of_yes_answers.append(yesCount)
    else :
        line = line.rstrip()
        current_section_array.append(line)

print("Total Sum of Yes answers : {}".format(sum(number_of_yes_answers)))
