import re
with open('inputs/day_07.txt') as input:
    data = input.read().splitlines()

bag_dict = {}
for d in data:
    top_level_bag = d.split()[:2]
    top_level_bag = ' '.join(top_level_bag)
    inner_bags = re.sub('\d', '', d)
    inner_bags = inner_bags.split('contain')[1]
    inner_bags = inner_bags.replace('bags', '')
    inner_bags = inner_bags.replace('bag', '')
    bag_dict[top_level_bag] = inner_bags


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
stay_gold = len(set(bag_list))

# part two --------------------------------------------------------------------
bag_dict_two = {}
for d in data:
    top_level_bag = d.split()[:2]
    top_level_bag = ' '.join(top_level_bag)
    inner_bags = d.split('contain')[1][1:]
    inner_bags = inner_bags.replace('bags', '')
    inner_bags = inner_bags.replace('bag', '')
    inner_bags = inner_bags.replace(' , ', ',')
    inner_bags = inner_bags.replace(' .', '')
    inner_bags = inner_bags.replace('.', '')
    bag_dict_two[top_level_bag] = inner_bags

bags_to_traverse = []
initial_multipliers = []
multipliers = {}
bags_traversed = {}
for key, value in bag_dict_two.items():
    if key == 'shiny gold':
        bags_string = (value.split(','))
        for b in bags_string:
            initial_multipliers.append(b[0])
            bags_to_traverse.append(b[2:])
        for bag in bags_to_traverse: # highest level bags
            bags_traversed[bag] = None
            multipliers[bag] = None
            for key, value in bag_dict_two.items():
                  if key == bag:
                      bags_string_two = (value.split(',')) # get the bags in that bag
                      bags_in_bag = []
                      counts_of_bags = []
                      for b in bags_string_two:
                          bags_in_bag.append(b[2:])
                          counts_of_bags.append(b[0])
                          bags_to_traverse.append(b[2:])
                      bags_traversed[bag] = bags_in_bag
                      multipliers[bag] = counts_of_bags

# might need to replace the values of 'other' and 'n'
print(multipliers)
print(type(multipliers))

lets_go = ['dim beige', 'dark maroon', 'light blue']

bags_to_add = []
for key, value in bags_traversed.items():
    if key in lets_go:
        bags_to_add.append(value)
        for bag in bags_to_add:
            for key, value in bags_traversed.items():
                if bag == key:
                    bags_to_add.append(value)
            #multiply by top level bag add bags in bag
            #bag_total = multipliers[bag]
        #print(multipliers[bag])



#print(bags_traversed)
#print(multipliers)




