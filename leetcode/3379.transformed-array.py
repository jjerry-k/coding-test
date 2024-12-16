#
# @lc app=leetcode id=3379 lang=python3
#
# [3379] Transformed Array
# Your runtime beats 47.77 % of python3 submissions
# Your memory usage beats 96.96 % of python3 submissions (17.2 MB)
# @lc code=start
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        for i, v in enumerate(nums):
            result[i] = nums[(i+v)%n]
        return result       
# @lc code=end