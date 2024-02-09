#
# @lc app=leetcode id=2894 lang=python3
#
# [2894] Divisible and Non-divisible Sums Difference
# Your runtime beats 84.04 % of python3 submissions
# Your memory usage beats 72.82 % of python3 submissions (16.6 MB)
# @lc code=start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        result = 0
        for i in range(1, 1+n):
            if i%m:
                result += i
            else:
                result -= i
        return result
# @lc code=end