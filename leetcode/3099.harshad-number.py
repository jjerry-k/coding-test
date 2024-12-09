#
# @lc app=leetcode id=3099 lang=python3
#
# [3099] Harshad Number
# 100/100 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 5.99 % of python3 submissions (17.6 MB)
# @lc code=start
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digits = sum(int(str(i)) for i in str(x))
        return -1 if x % sum_of_digits else sum_of_digits
# @lc code=end