with open('inputs/day_ten.txt') as f:
    joltage_ratings = f.read().splitlines()
    joltage_ratings = [int(j) for j in joltage_ratings]
    joltage_ratings.sort()

diffs = []
for i, rating in enumerate(joltage_ratings):
    if i < len(joltage_ratings) - 1:
        diffs.append(joltage_ratings[i+1] - joltage_ratings[i])

output = (diffs.count(1) + 1) * (diffs.count(3) + 1) # account for wall to port and end of port chain to device
print(output)

# part two --------------------------------------------------------------------

