import numpy

"""
(2/19/2020 diagonal_sort)
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then
return the sorted array.
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
import collections

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
    buckets = [[0 for col in range(width)] for row in range(height)]
    for value in buckets:
        print(value)
    print(" ----- ")
    for index, element in enumerate(flat_sorted_array):
        coordinate = fringe_left_outer[index]
        buckets[coordinate[0]][coordinate[1]] = element[0]
        cur_cordinate_x = coordinate[0]
        cur_cordinate_y = coordinate[1]
        try:
            for index2, arr_val in enumerate(element):
                if index2 != 0:
                    buckets[cur_cordinate_y][cur_cordinate_x] = arr_val
                    cur_cordinate_x += 1
                    cur_cordinate_y += 1
        except IndexError:
            continue
    for value in buckets:
        print(value)


"""
(2/20/2020 can_visit_all_rooms)
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have 
some keys to access the next room. 
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = 
rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0). 
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.
Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
"""

# strategy: make an array of length of rooms, fill with zeros, as rooms can be moved to, fill with a number, if 0  at
# end, return a false


def can_visit_all_rooms(self, rooms):
    size = len(rooms)
    rooms_visited = [False for i in range(size)]
    available_room = {0}

    while available_room:
        current_room = available_room.pop()
        rooms_visited[current_room] = True

        for room_with_key in rooms[current_room]:
            if not rooms_visited[room_with_key]:
                available_room.add(room_with_key)
    print(rooms_visited)
    if False in rooms_visited:
        print("False")
    else:
        print("True")



