# with open('input.txt', 'r') as file:
#     lines = [line.rstrip('\n') for line in file.readlines()]
#
# master_list = []
#
# def put_in_lists():
#     for line in lines:
#         test = line.split()
#         master_list.append(test)
#     for group in master_list:
#         i = 0
#         while i < len(group):
#             group[i] = int(group[i])
#             i += 1
#
#
# def check_order(lst):
#     """Checks if a list of numbers is ascending, descending, or neither."""
#
#     if all(lst[i] < lst[a + 1] for a in range(len(lst) - 1)):
#         return True, "ascending"
#     elif all(lst[i] > lst[a + 1] for a in range(len(lst) - 1)):
#         return True, "descending"
#     else:
#         return False, "neither"
#
#
# put_in_lists()
# safe_reports = 0
#
# for report in master_list:
#     i = 0
#     j = 1
#     safe, direction = check_order(report)
#     if direction == "neither":
#         for number in report:
#
#     if safe and direction == "ascending":
#         while j < len(report):
#             if report[j] - report[i] < 1 or report[j] - report[i] > 3:
#                 safe = False
#             elif report[j] == report[i]:
#                 safe = False
#             i += 1
#             j += 1
#         if safe:
#             safe_reports += 1
#     if safe and direction == "descending":
#         while j < len(report):
#             if report[i] - report[j] < 1 or report[i] - report[j] > 3:
#                 safe = False
#             elif report[i] == report[j]:
#                 safe = False
#             i += 1
#             j += 1
#         if safe:
#             safe_reports += 1
#
# print(safe_reports)

asc = "ASC"
desc = "DESC"
tolerance = 3


def get_lines(test=False):
    with open(("test" if test else "input") + ".txt") as file:
        for ln in file:
            yield ln.strip()


def check_numbers(type, first, second):
    """checks if number ascend or descend and are within a tolerance range"""
    global asc, desc
    type = type or (asc if first < second else desc)
    return (type, adheres_to_rules(type, first, second))


def adheres_to_rules(type, first, second):
    """ensures tolerance and asc / desc rules are followed"""
    global asc, desc, tolerance
    return not (
        (type == asc and (second <= first or second > first + tolerance))
        or (type == desc and (second >= first or second < first - tolerance))
    )


def is_safe(numbers, problem_dampener_disabled=True, problem_dampener_used=False):
    """
    recursive
    checks if a set of numbers is safe according to the puzzle rules
    """
    type = None
    for ii, num in enumerate(numbers):
        if ii >= len(numbers) - 1:
            return True
        (type, success) = check_numbers(type, num, numbers[ii + 1])
        if not success:
            break

    return (
        False
        if problem_dampener_disabled or problem_dampener_used
        else check_safe_with_elements_removed(numbers)
    )


def check_safe_with_elements_removed(numbers):
    """tries to find a safe solution with one of the numbers missing"""
    for ii in range(len(numbers)):
        if is_safe(
            numbers[:ii] + numbers[ii + 1 :],
            problem_dampener_disabled=False,
            problem_dampener_used=True,
        ):
            return True
    return False


def solution_1():
    return sum(
        [1 if is_safe(list(map(int, line.split()))) else 0 for line in get_lines()]
    )


def solution_2():
    return sum(
        [
            (
                1
                if is_safe(
                    list(map(int, line.split())), problem_dampener_disabled=False
                )
                else 0
            )
            for line in get_lines()
        ]
    )


print("1:", solution_1())
print("2:", solution_2())