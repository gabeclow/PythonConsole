
"""
(2/14/2020 reverse_words)
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""


# (2/14/2020 reverse_words)
def reverse_words(s):
    result = ""
    total_string = s.split()
    for word in total_string:
        result += word[::-1] + " "
    return result
