
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
                    if island_array[index + 1][square_index] == 0:  # if tile below is ocean, increase counter
                        counter += 1
                except IndexError:
                    counter += 1
                try:
                    if island_array[index - 1][square_index] == 0:  # if tile above is ocean, increase counter
                        counter += 1
                except IndexError:
                    counter += 1
                try:
                    if island_array[index][square_index + 1] == 0:  # if tile on right is ocean, increase counter
                        counter += 1
                except IndexError:
                    counter += 1
                try:
                    if island_array[index][square_index - 1] == 0:  # if tile on left is ocean, increase counter
                        counter += 1
                except IndexError:
                    counter += 1
    print(str(counter))
    return counter


def is_armstrong_num(self, num):
    result = 0
    num_array = []
    num_of_nums = 0
    calculation = num
    while calculation % 10 > 0:
        num_of_nums += 1
        num_array.append(calculation % 10)
        calculation = calculation/10
        calculation = calculation.__trunc__()

    for number in num_array:
        result += number ** num_of_nums
    if num == result:
        return True
    else:
        return False


def score_from_2d_arr(self, arr):
    dic = {}
    for num_set in arr:
        if dic.__contains__(num_set[0]):
            value = dic[num_set[0]]
            value[1] = value[1] + 1
            value[0] += num_set[1]
            dic[num_set[0]] = value
            # value = dic[num_set[0]]
            # dic[num_set[0]] = [num_set[1] + dic[num_set[0]]][value + 1]
        else:
            dic[num_set[0]] = [num_set[1], 1]
    for key, number_set in dic.items():
        print(number_set[0] / number_set[1])


def common_chars(s_array):
    for word in s_array:
        dictionary = collections.Counter(word)
    print(dictionary)


