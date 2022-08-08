#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
# Your runtime beats 84.1 % of python3 submissions
# Your memory usage beats 43.28 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
# @lc code=end