with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

distance_list = []
distance_total = 0

def convert_to_list(num_1, num_2):
    num_1_list = []
    num_2_list = []
    for num in num_1:
        num_1_list.append(int(num))
    for num in num_2:
        num_2_list.append(int(num))
    num_1_list.sort()
    num_2_list.sort()
    return num_1_list, num_2_list


def find_distances(list_1, list_2):



for pair in lines:
    thing_one, thing_two = pair.split()
    thing_1, thing_2 = convert_to_list(thing_one, thing_two)
    print(thing_1, thing_2)

