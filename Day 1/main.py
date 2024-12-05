with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

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
    distance_list = []
    i = 0
    for num in list_1:
        if num > list_2[i]:
            distance = num - list_2[i]
            i += 1
            distance_list.append(distance)
        else:
            distance = list_2[i] - num
            i += 1
            distance_list.append(distance)
    return distance_list


answer = 0
total_distance = []

for pair in lines:
    thing_one, thing_two = pair.split()
    thing_1, thing_2 = convert_to_list(thing_one, thing_two)

    all_5_distances = find_distances(thing_1, thing_2)

    list_total = sum(all_5_distances)
    answer += list_total

print(answer)

