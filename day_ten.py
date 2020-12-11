with open('inputs/day_ten.txt') as f:
    joltage_ratings = f.read().splitlines()
    joltage_ratings = [int(j) for j in joltage_ratings]
    joltage_ratings.sort()

diffs = []
for i, rating in enumerate(joltage_ratings):
    if i < len(joltage_ratings) - 1:
        diffs.append(joltage_ratings[i+1] - joltage_ratings[i])

output = (diffs.count(1) + 1) * (diffs.count(3) + 1) # account for wall to port and end of port chain to device
#print(output)

# part two --------------------------------------------------------------------

# multiply paths together
print(joltage_ratings)
print(diffs)

# the 3s are sticking points, so do combinations of numbers before and after them
# to gate through the 3s
# get to 4 -- 7 (1)(2)(3)(1, 2)(1, 3)(2, 3)
# get to 14 -- 7 (11, 12)
# get to 20 -- 4
# get to 27 -- 7
# get to 34 -- 7
# get to 39 -- 2
# get to 53 -- 7
# get to 60 -- 7
# get to 67 -- 7
# get to 74 -- 7
# get to 81 -- 7
# get to 95 -- 7
# get to 109 -- 7
# get to 119 -- 7
# get to 131 -- 4 (0)(129)(130)(129, 130)
# get to 136 -- 2
# get to 141 -- 2
# get to 148 -- 7
# get to 155 -- 7

# So, (7**14 * 4**2 * 2**3)
