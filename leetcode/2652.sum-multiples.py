#
# @lc app=leetcode id=2652 lang=python3
#
# [2652] Sum Multiples
# Your runtime beats 97.39 % of python3 submissions
# Your memory usage beats 59.88 % of python3 submissions (16.3 MB)
# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum([i for i in range(1, n+1) if (not i%3) or (not i%5) or (not i%7)])
# @lc code=end