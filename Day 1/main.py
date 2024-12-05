with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

answer = 0
distance_list_1 = []
distance_list_2 = []

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
    i = 0
    score = 0
    for _ in range(len(list_1)):
        score += abs(list_2[i] - list_1[i])
        i += 1
    return score


for pair in lines:
    thing_one, thing_two = pair.split()
    # thing_1, thing_2 = convert_to_list(thing_one, thing_two)
    distance_list_1.append(int(thing_one))
    distance_list_2.append(int(thing_two))

    distance_list_1.sort()
    distance_list_2.sort()

    answer = find_distances(distance_list_1, distance_list_2)

print(answer)

