import numpy as np

from my_packages.my_functions.list_functions import selection_sort


def create_list_from_list_diagonal(matrix):
    idx = 0
    while idx < len(matrix):
        if (idx + 1) != len(matrix):
            if len(matrix[idx]) == len(matrix[idx + 1]):
                idx += 1
                continue
            else:
                print("The matrix isn't square!")
                return
        else:
            break
    idx = 0
    j = len(matrix[0]) - 1
    new_list = []
    while idx < len(matrix):
        new_list.append(matrix[idx][j])
        idx += 1
        j -= 1
    return new_list


def move_elements(list: list, num_of_elms, mov_from, mov_to):
    """
    :param mov_to:
    :param mov_from:
    :param num_of_elms:
    :type list: list
    """
    if num_of_elms <= 0:
        return
    if mov_from >= 0 and mov_to < len(list):
        if mov_from + num_of_elms > len(list):
            to = mov_from - num_of_elms
            mov_elem_list = list[to:mov_from]
            list = list[:to] + list[mov_from:]
            for j in range(len(mov_elem_list)):
                list.insert(mov_to + j, mov_elem_list[j])
            return list
        to = mov_from + num_of_elms
        mov_elem_list = list[mov_from:to]
        list = list[:mov_from] + list[to:]
        for j in range(len(mov_elem_list)):
            list.insert(mov_to, mov_elem_list[j])
            mov_to = mov_to + 1
    return list


matrix_4x4 = np.array([[1, 3, 4, 7],
                       [3, 6, 2, 3],
                       [1, 0, 3, 4],
                       [1, 2, 3, 4]])
print(matrix_4x4)
create_list_from_list_diagonal(matrix_4x4)

list1 = []
print("List 1  = ", list1)

list2 = [5, 4, 'string', list1]
print("List 2  = ", list2)

list2_copy = list2[:]
list_2_list_copy = list(list2)
pre_list_output_formatter = "%-20s"
list_output_formatter = "%-{}s".format(len(str(list2)) + 3)
id_output_formatter = "%-20s"

output_lists = [
    [f"list 2 = ", list2, "id = {}".format(id(list2))],
    [f"Copy list 2([:]) = ", list2_copy, "id = {}".format(id(list2_copy))],
    [f"Copy list 2([:]) = ", list_2_list_copy, "id = {}".format(id(list_2_list_copy))],
]
for row in output_lists:
    print(pre_list_output_formatter % row[0] + list_output_formatter % row[1] + id_output_formatter % row[2])

list2 += list2_copy

print("List 2 + list 2 copy  = ", list2)
print("Zero element of list 2  =", list2[0])

list1 += 3, 5, 6
list2[1] = list1

print("1 element of list 2 changed to list 1  = ", list2)

list2.remove(list2[2])
print("Remove 2 element from list 2  = ", list2)

print("Max element of list 1 = ", max(list1))

i = [22, ['ogo', 3, 88], 'apple']
print("This is 88  - ", i[1][2])

list3 = list2[int(len(list2) / 2):]
print("list 3 = " + str(list3))

print(move_elements(list2, 3, 5, 1))

n_sorted_list = [5, 6, 7, 7, 5, 43, 2, 3, 5, 6, 7, 9, 9, 9, 7, 43, 2, 0]

sorted_list = selection_sort(n_sorted_list)
print(f"sorted list = {sorted_list}")
'''
for i in range(len(sorted_list)):
    print(sorted_list[i])
'''
for i in sorted_list:
    print(i, end=' ')

list_sum = 0
for i in sorted_list:
    list_sum = list_sum + i
print(f"\nlist sum = {list_sum}")

hello_list = 'Hello'

hello_3 = [symb * 3 for symb in hello_list]
print(hello_3)
