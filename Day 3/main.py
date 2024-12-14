import re
find_all_examples = []
total = 0

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

master_list = []

for string in lines:
    master_list.append(string)

for string in master_list:
    find_all_examples = re.findall('mul\(\d{1,3},\d{1,3}\)', string)

for example in find_all_examples:
    numbers = re.findall('\d{1,3},\d{1,3}', example)
    print(numbers)

    num_1 = numbers[0]
    num_2 = numbers[1]
    value = num_1 * num_2
    total += value

print(total)