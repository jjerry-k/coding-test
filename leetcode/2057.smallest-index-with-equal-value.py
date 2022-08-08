#
# @lc app=leetcode id=2057 lang=python3
#
# [2057] Smallest Index With Equal Value
# Your runtime beats 56.86 % of python3 submissions
# Your memory usage beats 56.11 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i
        return -1
# @lc code=end