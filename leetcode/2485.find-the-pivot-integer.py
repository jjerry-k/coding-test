#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
# Your runtime beats 99.08 % of python3 submissions
# Your memory usage beats 53.24 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = (n * (n + 1)) // 2
        if total_sum % (total_sum**0.5) == 0:
            return int(total_sum**0.5)
        return -1
# @lc code=end