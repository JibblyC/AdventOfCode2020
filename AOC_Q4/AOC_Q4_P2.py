from AOC_Q4_P2_Helper import check_credential_is_valid
import re

input_array = []
correct_credentials_list = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
current_section_array = []
correctPassports = 0

with open("AOC_Q4/Q4_input.txt") as my_file:
    input_array = my_file.readlines()

for line in input_array:
    if line == "\n":
        correctHits = 0
        for lineToCheckCreds in current_section_array:
            for credential in correct_credentials_list:
                if credential in lineToCheckCreds:  
                    if check_credential_is_valid(credential,lineToCheckCreds):               
                        correctHits += 1
        if correctHits == len(correct_credentials_list):
            correctPassports += 1
        current_section_array.clear()
    else :
        current_section_array.append(line)

print("Number of correct passports: {}".format(correctPassports))





