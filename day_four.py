with open('inputs/day_four.txt') as input:
    data = input.read()

passports = data.split('\n\n')
passports = [str.replace(passport, '\n',' ') for passport in passports]

valid_passports = 0
for passport in passports:
    count = passport.count(' ')
    if count == 7:
        valid_passports += 1
    elif count == 6 and 'cid:' not in passport:
        valid_passports += 1
    else:
        continue

print(valid_passports)
