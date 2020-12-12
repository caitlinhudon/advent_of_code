with open('inputs/day_11_example.txt') as f:
    seats = f.read().splitlines()

# (.) Floor, L empty, # occupied
# Seat empty and no occupied seats adjacent, becomes occupied
# Seat occupied and four or more adjacent also occupied, seat becomes empty

# 1 2 3
# 4 X 5   <--- surrounding seats, numbered
# 7 8 9

upper_row_index = len(seats) - 1

seat_map = seats
new_seat_map = seats

i = 0
while i < 6:
    seat_map = new_seat_map
    new_seat_map = []
    for ri, row in enumerate(seat_map):
        upper_seat_index = len(row) - 1
        row_list = []
        for si, seat in enumerate(row):
            surrounding_seats = [None] * 8
            if ri > 0 and ri < upper_row_index and si > 0 and si < upper_seat_index:
                surrounding_seats = [seat_map[ri - 1][si - 1], seat_map[ri - 1][si], seat_map[ri - 1][si + 1],
                                     seat_map[ri][si - 1], seat_map[ri][si + 1],
                                     seat_map[ri + 1][si - 1], seat_map[ri + 1][si], seat_map[ri + 1][si + 1]]
            if ri == 0 and si > 0 and si < upper_seat_index:
                surrounding_seats = [None, None, None,
                                     seat_map[ri][si - 1], seat_map[ri][si + 1],
                                     seat_map[ri + 1][si - 1], seat_map[ri + 1][si], seat_map[ri + 1][si + 1]]
            if ri == upper_row_index and si > 0 and si < upper_seat_index:
                surrounding_seats = [seat_map[ri - 1][si - 1], seat_map[ri - 1][si], seat_map[ri - 1][si + 1],
                                     seat_map[ri][si - 1], seat_map[ri][si + 1],
                                     None, None, None]
            if si == 0 and ri > 0 and ri < upper_row_index:
                surrounding_seats = [None, seat_map[ri - 1][si], seat_map[ri - 1][si + 1],
                                     None, seat_map[ri][si + 1],
                                     None, seat_map[ri + 1][si], seat_map[ri + 1][si + 1]]
            if si == upper_seat_index and ri > 0 and ri < upper_row_index:
                surrounding_seats = [seat_map[ri - 1][si - 1], seat_map[ri - 1][si], None,
                                     seat_map[ri][si - 1], None,
                                     seat_map[ri + 1][si - 1], seat_map[ri + 1][si], None]
            if ri == 0 and si == 0:
                surrounding_seats = [None, None, None,
                                     None, seat_map[ri][si + 1],
                                     None, seat_map[ri + 1][si], seat_map[ri + 1][si + 1]]
            if ri == upper_row_index and si == 0:
                surrounding_seats = [None, seat_map[ri - 1][si], seat_map[ri - 1][si + 1],
                                     None, seat_map[ri][si + 1],
                                     None, None, None]
            if ri == 0 and si == upper_seat_index:
                surrounding_seats = [None, None, None,
                                     seat_map[ri][si - 1], None,
                                     seat_map[ri + 1][si - 1], seat_map[ri + 1][si], None]
            if ri == upper_row_index and si == upper_seat_index:
                surrounding_seats = [seat_map[ri - 1][si - 1], seat_map[ri - 1][si], None,
                                     seat_map[ri][si - 1], None,
                                     None, None, None]
            if seat_map[ri][si] == '.':
                row_list.append('.')
            elif surrounding_seats.count('L') == 0:
                row_list.append('#')
            elif surrounding_seats.count('#') >= 4:
                row_list.append('L')
            else:
                continue
        new_seat_map.append(row_list)
        if new_seat_map == seat_map:
            output = new_seat_map
            break
    i += 1
print(output)
print(output.count('#'))
