with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

answer = 0
distance_list_1 = []
distance_list_2 = []

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

for num in distance_list_1:
    count = 0
    for digit in distance_list_2:
        if num == digit:
            count += 1
    answer += num * count

print(answer)

