#
# @lc app=leetcode id=2413 lang=python3
#
# [2413] Smallest Even Multiple
# Your runtime beats 86.86 % of python3 submissions
# Your memory usage beats 99.74 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n%2==0 else n*2
# @lc code=end