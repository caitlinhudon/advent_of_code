import math
with open('inputs/day_three.txt') as input:
    grid = input.read().splitlines()

row = 0
column = 0
trees = 0
for g in grid:
    if row > 9:
        expansions = math.ceil(column / 30)
        expanded_g = g * expansions
    else:
        expanded_g = g
    if expanded_g[column] == '#':
        trees += 1
    row += 1
    column += 3

print(trees)
