import re

with open('inputs/day_seven.txt') as input:
    data = input.read().splitlines()

# How many bag colors can eventually contain at least one shiny gold bag?

# make a dict with key = top level bag, values = next level bag
bag_dict = {}
for d in data:
    top_level_bag = d.split()[:2]
    top_level_bag = ' '.join(top_level_bag)
    inner_bags = re.sub('\d', '', d)
    inner_bags = inner_bags.split('contain')[1]
    inner_bags = inner_bags.replace('bags', '')
    inner_bags = inner_bags.replace('bag', '')
    bag_dict[top_level_bag] = inner_bags # create keys (top level bags) of dict


def check_bags(bag_color='shiny gold'):
    bags_to_check = []
    good_bags = []
    for key, value in bag_dict.items():
        if bag_color in value:
            good_bags.append(key)
            bags_to_check.append(key)
    for next_bag in bags_to_check:
        for key, value in bag_dict.items():
            if next_bag in value:
                good_bags.append(key)
                bags_to_check.append(key)
    return(good_bags)

bag_list = check_bags()
best_bags = set(bag_list)

print(len(best_bags))

