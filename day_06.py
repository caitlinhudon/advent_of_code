from collections import Counter

with open('inputs/day_06.txt') as input:
    data = input.read()

group_answers_raw = data.split('\n\n')
group_answers = [str.replace(answer, '\n','') for answer in group_answers_raw]

all_counts = []
for answer in group_answers:
    count = len(Counter(answer))
    all_counts.append(count)

print(sum(all_counts))

# part two --------------------------------------------------------------------

group_answers_two = [str.replace(answer, '\n',' ') for answer in group_answers_raw]

all_answered = []
for answer in group_answers_two:
    counted = Counter(answer)
    people = counted[' '] + 1
    all_answered_qs = {x: count for x, count in counted.items() if count == people}
    all_answered.append(len(all_answered_qs))

print(sum(all_answered))