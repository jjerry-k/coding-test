#
# @lc app=leetcode id=2154 lang=python3
#
# [2154] Keep Multiplying Found Values by Two
# Your runtime beats 84.05 % of python3 submissions
# Your memory usage beats 91.15 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while 1:
            if original not in nums:
                return original
            else:
                original *= 2
# @lc code=end