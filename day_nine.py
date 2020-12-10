from itertools import combinations

with open('inputs/day_nine.txt') as f:
    xmas_data = f.read().splitlines()


combos = list(combinations(range(25), 2)) # 25 values from positions 0 to 24
i_values = list(range(len(xmas_data)))

is_a_sum = list([0] * (len(xmas_data)))
print(is_a_sum)
print(type(is_a_sum))

for i in range(len(xmas_data)):
    if i > 24:
        data = xmas_data[i - 25:i]
        for c in list(combos):
            if int(data[c[0]]) + int(data[c[1]]) == int(xmas_data[i]):
                is_a_sum[i] += 1

for index, value in enumerate(is_a_sum):
    if value == 0 and index > 24:
        print(index, value)

print(xmas_data[561])

# part two --------------------------------------------------------------------


