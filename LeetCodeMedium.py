"""
(2/19/2020 diagonal_sort)
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Before
[3,3,1,1]
[2,2,1,2]
[1,1,1,2]
After
[1,1,1,1]
[1,2,2,2]
[1,2,3,3]
"""
import numpy


def diagonal_sort(self, mat):
    for row in mat:
        print(row)
    # assume that mat is not a jagged array.
    height = len(mat)
    width = len(mat[0])
    print("height: " + str(height))
    print("width: " + str(width))
    diag_array = []
    fringe_left_outer = []
    for num in range(width):
        fringe_left_outer.append([0, num])
    for num in range(1, height):
        fringe_left_outer.append([num, 0])

    print(fringe_left_outer)

    for index_item in fringe_left_outer:
        _list = index_item[0]
        el_in_list = index_item[1]
        flag_inner = True
        while flag_inner:
            try:
                diag_array.append(mat[_list][el_in_list])
                _list += 1
                el_in_list += 1
            except IndexError:
                flag_inner = False
                diag_array.append(-1)
    # print(diag_array)
    temp_array = []
    sorted_array = []
    for item in diag_array:
        if item != -1:
            temp_array.append(item)
        if item == -1:
            temp_array.sort()
            sorted_array.append(temp_array)
            temp_array = []
    print(sorted_array)
    np_array = numpy.array(sorted_array)
    flat_sorted_array = numpy.ndarray.flatten(np_array)
    buckets = [[0 for col in range(4)] for row in range(3)]
    for value in buckets:
        print(value)
    for index, element in enumerate(flat_sorted_array):
        coordinate = fringe_left_outer[index]
        buckets[coordinate[0]][coordinate[1]] = element
    for value in buckets:
        print(value)