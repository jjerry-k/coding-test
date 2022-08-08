#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
# Your runtime beats 88.44 % of python3 submissions
# Your memory usage beats 49.09 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = 0
        for num in set(nums):
            result += num if nums.count(num) == 1 else 0
        return result
# @lc code=end