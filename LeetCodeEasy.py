
"""
(2/14/2020 reverse_words)
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""


# (2/14/2020 reverse_words)
import collections


def reverse_words(s):
    result = ""
    total_string = s.split()
    for word in total_string:
        result += word[::-1] + " "
    return result


"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4"""


def single_number(self, nums):
    num_dictionary = collections.Counter(nums)
    for key, value in num_dictionary.items():
        if value == 1:
            print(str(key) + " was found " + str(value) +" time.")
    print(num_dictionary)


def single_number_v2(self, nums):
    seen = {}
    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    for num in seen:
        if seen[num] == 1:
            return num


def island_perimeter(self, island_array):
    counter = 0
    height = len(island_array)
    width = len(island_array[0])
    for index, row in enumerate(island_array):
        for square_index, square in enumerate(row):
            if square == 0: # we don't count perimeter of water
                continue
            else:

                try:
                    if island_array[index + 1][square_index] == 0: # if tile below is ocean, increase counter
                        counter += 1
                except IndexError:
                    counter += 1
                try:
                    if island_array[index - 1][square_index] == 0: # if tile above is ocean, increase counter
                        counter += 1
                except IndexError:
                    counter += 1
                try:
                    if island_array[index][square_index + 1] == 0 : # if tile on right is ocean, increase counter
                        counter += 1
                except IndexError:
                    counter += 1
                try:
                    if island_array[index][square_index - 1] == 0: # if tile on left is ocean, increase counter
                        counter += 1
                except IndexError:
                    counter += 1
    print(str(counter))
    return counter

