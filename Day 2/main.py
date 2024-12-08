with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

master_list = []

def put_in_lists():
    for line in lines:
        test = line.split()
        master_list.append(test)
    for group in master_list:
        i = 0
        while i < len(group):
            group[i] = int(group[i])
            i += 1


def check_order(lst):
    """Checks if a list of numbers is ascending, descending, or neither."""

    if all(lst[i] < lst[a + 1] for a in range(len(lst) - 1)):
        return True, "ascending"
    elif all(lst[i] > lst[a + 1] for a in range(len(lst) - 1)):
        return True, "descending"
    else:
        return False, "neither"


put_in_lists()
safe_reports = 0

for report in master_list:
    i = 0
    j = 1
    safe, direction = check_order(report)
    if safe and direction == "ascending":
        while j < len(report):
            if report[j] - report[i] < 1 or report[j] - report[i] > 3:
                safe = False
            elif report[j] == report[i]:
                safe = False
            i += 1
            j += 1
        if safe:
            safe_reports += 1
    if safe and direction == "descending":
        while j < len(report):
            if report[i] - report[j] < 1 or report[i] - report[j] > 3:
                safe = False
            elif report[i] == report[j]:
                safe = False
            i += 1
            j += 1
        if safe:
            safe_reports += 1

print(safe_reports)