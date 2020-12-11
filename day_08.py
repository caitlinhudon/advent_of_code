with open('inputs/day_08.txt') as f:
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

instructions_two = instructions

def run_the_loop():
    accumulator_values = []
    next_checks = [0]
    visited_count = [0] * len(instructions_two)

    for i, next_check in enumerate(next_checks):
        for index, value in enumerate(instructions_two):
            if any(x > 1 for x in visited_count):
                return(0)
            if next_check == index:
                direction = value[:3]
                n = value[4:]
                if direction == 'jmp':
                    accumulator_values.append(0)
                    next_checks.append(index + int(n))
                elif direction == 'acc':
                    accumulator_values.append(int(n))
                    next_checks.append(index + 1)
                else:  # nop
                    accumulator_values.append(0)
                    next_checks.append(index + 1)
                visited_count[index] += 1
    return(sum(accumulator_values))

for i in range(len(instructions_two)):
    if 'nop' in instructions_two[i]:
        instructions_two[i] = instructions_two[i].replace('nop', 'jmp')
        print(instructions_two[i], run_the_loop())
        instructions_two[i] = instructions_two[i].replace('jmp', 'nop')

for i in range(len(instructions_two)):
    if 'jmp' in instructions_two[i]:
        instructions_two[i] = instructions_two[i].replace('jmp', 'nop')
        print(instructions_two[i], run_the_loop())
        instructions_two[i] = instructions_two[i].replace('nop', 'jmp')


