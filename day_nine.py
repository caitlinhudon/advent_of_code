from itertools import combinations

with open('inputs/day_nine.txt') as f:
    xmas_data = f.read().splitlines()


combos = list(combinations(range(25), 2)) # 25 values from positions 0 to 24
i_values = list(range(len(xmas_data)))

is_a_sum = list([0] * (len(xmas_data)))

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

# brute force ftw lately :shrug:
def find_addends():
    for combo_length in range(len(xmas_data)):
        if combo_length > 2:
            for i in range(len(xmas_data)):
                if i > 2:
                    data = xmas_data[i:(i+combo_length)]
                    data = [int(d) for d in data]
                    data_total = sum(data)
                    if data_total == 70639851:
                        return sorted(data)

output_list = find_addends()
output = output_list[0] + output_list[len(output_list) - 1]
