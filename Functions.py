import collections
from itertools import permutations
import numpy


def is_palindrome(x):
    x_copy = x
    rev = 0
    while x > 0:
        a = x % 10
        rev = rev * 10 + a
        x = x / 10
    if x_copy == rev:
        return 1


def is_palindrome_s(variable):
    original_value = str(variable)
    return original_value[::-1] == original_value


def recursive_factorial(num):
    if num <= 1:
        return num
    return num * recursive_factorial(num - 1)


def recursive_fibonacci_at_index(number):
    if number <= 1:
        return number
    else:
        return recursive_fibonacci_at_index(number - 1) + recursive_fibonacci_at_index(number - 2)


def create_set():
    print()


def switch(x):
    return {
        1: "type1",
        2: "type2",
        3: "type3",
        4: "type4",
    }.get(x, "null")


def index_of_code(string, search_for):
    search_length = len(search_for)

    for pos, char in enumerate(string):
        if search_for[0] == char:
            slice_to = pos + search_length
            found_word = string[pos: slice_to]
            if str(found_word) == str(search_for):
                return pos


def py_index_of(string, search_for):
    return string.index(search_for)


"""
(2020.12 Robot)
There is a robot starting at position (0, 0), the origin, on a 2D plane. 
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
The move sequence is represented by a string, and the character moves[i] represents its ith move. 
Valid moves are R (right), L (left), U (up), and D (down). 
If the robot returns to the origin after it finishes all of its moves, return true. 
Otherwise, return false.
"""


def judge_circle(self, moves):  # see 2020.12 Robot
    up = 0
    down = 0
    right = 0
    left = 0
    for index, move in enumerate(moves):
        if move == "U":
            up += 1
        elif move == "D":
            down += 1
        elif move == "R":
            right += 1
        else:
            left += 1
    if up - down == 0 and right - left == 0:
        return True
    else:
        return False


def judge_circle_2(moves):
    counts = {'D': 0, 'U': 0, 'L': 0, 'R': 0}
    for move in moves:
        counts[move] += 1
    return counts['L'] == counts['R'] and counts['U'] == counts['D']


"""
(2020.12 Grid Description)
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. 
We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). 
Height 0 is considered to be a building as well. 
At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid.
A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. 
See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]
  
The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
"""


def line_max(grid):
    for row in grid:
        print(str(row))
    # print("Start Function")
    height = len(grid)
    width = len(grid[0])
    max_val_column_arr = []
    for row in range(0, width):
        max_val_col = 0

        for col in range(0, height):
            if max_val_col < grid[col][row]:
                max_val_col = grid[col][row]
        max_val_column_arr.append(max_val_col)
    print("Maxes: ")
    print(max_val_column_arr)

    max_val_row_arr = []
    for row in range(0, width):
        max_val_row = 0

        for col in range(0, height):
            if max_val_row < grid[row][col]:
                max_val_row = grid[row][col]
        max_val_row_arr.append(max_val_row)
    print(max_val_row_arr)
    print("Final Array: ")

    final_grid = [[0]*width for i in range(height)]
    for index, i in enumerate(grid):
        for index2, i2 in enumerate(i):
            if max_val_column_arr[index2] > max_val_row_arr[index]:
                final_grid[index][index2] = max_val_row_arr[index]
            else:
                final_grid[index][index2] = max_val_column_arr[index2]

    for row2 in final_grid:
        print(str(row2))

    initial_height = sum(list(numpy.array(grid).flat))
    final_height = sum(list(numpy.array(final_grid).flat))
    print("Initial height was: " + str(initial_height) + ". Final height was: " + str(final_height))
    return final_height - initial_height


def min_step_anagram_one_liner(s, t):
    print(sum((collections.Counter(s) - collections.Counter(t)).values()))


def min_step_anagram(original, change_to_anagram):
    dictionary_original = {}

    for index, i in enumerate(original):
        if i not in dictionary_original.keys():
            dictionary_original[i] = 1
        else:
            dictionary_original[i] += 1

    difference_count = 0
    for i in change_to_anagram:
        if i not in dictionary_original.keys():
            difference_count += 1
        elif dictionary_original[i] > 0:
            dictionary_original[i] -= 1
        else:
            difference_count += 1

    print(difference_count)


def num_tile_possibilities(self, tiles):
    tile_dictionary = collections.Counter(tiles)
    total_elements = len(str(tiles))
    repeating_elements = 0
    for values in tile_dictionary:
        if tile_dictionary[values] > 1:
            repeating_elements += tile_dictionary[values]

    a = recursive_factorial(total_elements)
    b = recursive_factorial(repeating_elements)
    c = a/b
    length = permutations(tiles, total_elements)
    print(length)


# "()))((" output should be 4
def min_parenthesis_to_add(self, s):
    left = 0
    right = 0
    for char in s:

        if char == "(":
            if right > 0:
                right -= 1
            else:
                left += 1

        elif char == ")":
            if left > 0:
                left -= 1
            else:
                right += 1
    print("test")
    return abs(left-right)


"""
def max_increase_(grid):  # see 2020.12 Grid Description
    for row in grid:
        print(str(row))

    length = len(grid)
    width = len(grid[0])
    print("length: " + str(length))
    print("width: " + str(width))

    pos = [0, 0]
    next_element = [0, 0]
    temp_max_row = 0
    temp_max_column = 0
    finished_row = False

    while pos != [length, width]:
        test1 = grid[(pos[0])][(pos[1])]
        test2 = grid[(next_element[0])][(next_element[1])]

        #  if covers the rows
        if not finished_row:
            if grid[(pos[0])][(pos[1])] <= grid[(next_element[0])][(next_element[1])]:
                if temp_max_row <= grid[(next_element[0])][(next_element[1])]:
                    temp_max_row = grid[(next_element[0])][(next_element[1])]

            if next_element[1] < width - 1:
                next_element[1] += 1

            if next_element[1] == 3:
                finished_row = True

        #  elif covers the columns
        if finished_row:
            if grid[(pos[1])][(pos[0])] <= grid[(next_element[1])][(next_element[0])]:
                if temp_max_column <= grid[(next_element[1])][(next_element[0])]:
                    temp_max_column = grid[(next_element[1])][(next_element[0])]

        else:
            next_element[0] = next_element[0] + 1
            next_element[1] = 0
            pos[0] = pos[0] + 1

    if pos[0] <= length:
        pos[0] += 1
    elif pos[1] <= width:
        pos[1] += 1
    else:
        pos = [length, width]
"""
