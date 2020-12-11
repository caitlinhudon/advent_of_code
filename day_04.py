import re

with open('inputs/day_04.txt') as input:
    data = input.read()

passports = data.split('\n\n')
passports = [str.replace(passport, '\n',' ') for passport in passports]

valid_passport_count = 0
valid_passports = []
for passport in passports:
    count = passport.count(' ')
    if count == 7:
        valid_passport_count += 1
        valid_passports.append(passport)
    elif count == 6 and 'cid:' not in passport:
        valid_passport_count += 1
        valid_passports.append(passport)
    else:
        continue

print(valid_passport_count)

# part two --------------------------------------------------------------------
# time for some fun with regex https://regexr.com/

valid_byr = 'byr:(19[2-9][0-9]|20[0][0-2])( *|$)'
valid_iyr = 'iyr:(20[1][0-9]|2020)( *|$)'
valid_eyr = 'eyr:(20[2][0-9]|2030)( *|$)'
valid_hgt = 'hgt:(1([5-8][0-9]|9[0-3])cm( *|$))|(5[9]|6[0-9]|7[0-6])in( *|$)'
valid_hcl = 'hcl:#([a-fA-F 0-9]{6})( *|$)'
valid_ecl = 'ecl:(amb|blu|brn|gry|grn|hzl|oth)( *|$)'
valid_pid = 'pid:[0-9]{9}( *|$)'
# # [cid doesn't matter']

valid_passport_count_two = 0
for v in valid_passports:
    count = passport.count(' ')
    if (re.search(valid_byr, v) is not None and
        re.search(valid_iyr, v) is not None and
        re.search(valid_eyr, v) is not None and
        re.search(valid_hgt, v) is not None and
        re.search(valid_hcl, v) is not None and
        re.search(valid_ecl, v) is not None and
        re.search(valid_pid, v) is not None):
        valid_passport_count_two += 1
    #print(v)
    #print(re.search(valid_byr, v))
    #print(re.search(valid_iyr, v))
    #print(re.search(valid_eyr, v))
    #print(re.search(valid_hgt, v))
    #print(re.search(valid_hcl, v))
    #print(re.search(valid_ecl, v))
    print(re.search(valid_pid, v))
print(valid_passport_count_two)
# 94 isn't the right answer
# 109 is too low
# 113 isn't correct
# 114 isn't correct
# 115 isn't correct
# 118 isn't correct
# 121 is correct
# 123 is too high
