from collections import Counter

with open('inputs/day_six.txt') as input:
    data = input.read()

group_answers = data.split('\n\n')
group_answers = [str.replace(answer, '\n','') for answer in group_answers]

all_counts = []
for answer in group_answers:
    count = len(Counter(answer))
    all_counts.append(count)

print(sum(all_counts))

# part two --------------------------------------------------------------------

