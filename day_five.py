with open('inputs/day_five.txt') as f:
    boarding_passes = f.read().splitlines()

seats = []
for bpass in boarding_passes:
    print(bpass)
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    for letter in range(len(bpass)):
        if letter <= 6:
            row_range = (max_row - min_row + 1) / 2
            if bpass[letter] == 'F':
                max_row = max_row - row_range
                min_row = min_row
            if bpass[letter] == 'B':
                max_row = max_row
                min_row = min_row + row_range
        if letter > 6:
            col_range = (max_col - min_col + 1) / 2
            if bpass[letter] == 'L':
                max_col = max_col - col_range
                min_col = min_col
            if bpass[letter] == 'R':
                max_col = max_col
                min_col = min_col + col_range
        final = min_row, max_row, min_col, max_col
        print(final)
        seat_id = (min_row * 8) + min_col
    seats.append(seat_id)

print(max(seats))

# part two --------------------------------------------------------------------

for r in range(978):
    if r not in sorted(seats):
        print(r)



