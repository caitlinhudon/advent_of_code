import math
with open('inputs/day_three.txt') as input:
    grid = input.read().splitlines()

def get_trees(over, down = 1):
    row = 0
    column = 0
    trees = 0
    for g in grid[::down]:
        if row > 3:
            expansions = math.ceil(column / 30)
            expanded_g = g * expansions
        else:
            expanded_g = g
        if expanded_g[column] == '#':
            trees += 1
        row += down
        column += over
    return trees

part_one_answer = get_trees(3)
part_two_answer = get_trees(1) * get_trees(3) * get_trees(5) * get_trees(7) * get_trees(1, 2)
print(part_one_answer)
print(part_two_answer)
