with open('inputs/day_eight.txt') as f:
    instructions = f.read().splitlines()

milestones = []
accumulator_values = []
next_checks = [0]
visited_count = [0] * len(instructions)
for i, next_check in enumerate(next_checks):
        for index, value in enumerate(instructions):
            if any(x > 1 for x in visited_count):
                break
            if next_check == index:
                direction = value[:3]
                n = value[4:]
                milestones.append(value)
                if direction == 'jmp':
                    accumulator_values.append(0)
                    next_checks.append(index + int(n))
                elif direction == 'acc':
                    accumulator_values.append(int(n))
                    next_checks.append(index + 1)
                else: # nop
                    accumulator_values.append(0)
                    next_checks.append(index + 1)
                visited_count[index] += 1

print(sum(accumulator_values[:-1]))

# part two --------------------------------------------------------------------

