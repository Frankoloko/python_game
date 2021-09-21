from random import randint

myarr = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]

# new_arr = []
# for index, item in enumerate(myarr):
#     percent = randint(1, 100)
#     if percent < 20:
#         myarr[index] = 9

# print(myarr)

# print(0.20 * 5)

change_percentage = 20
array_left = len(myarr)
random_changes = round(array_left * (change_percentage / 100))
used_indexes = []
for _ in range(random_changes):
    random_index = randint(0, array_left - 1)
    while random_index in used_indexes:
        random_index = randint(0, array_left - 1)
    used_indexes.append(random_index)
    myarr[random_index] = 9