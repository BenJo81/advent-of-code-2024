import re
find_all_examples = []
total = 0

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

master_list = []
master_list_2 = []

for string in lines:
    master_list.append(string)

for string in master_list:
    find_all_examples = re.findall('mul\(\d{1,3},\d{1,3}\)', string)
    master_list_2.append(find_all_examples)

for example in master_list_2:
    print(example)
    i = 0
    while i < len(example):
        numbers = re.findall('\d{1,3},\d{1,3}', example[i])
        print(numbers)
        num_1, num_2 = numbers[0].split(",")
        value = int(num_1) * int(num_2)
        total += value
        i += 1

print(total)