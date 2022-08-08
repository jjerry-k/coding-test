#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
# Your runtime beats 53.4 % of python3 submissions
# Your memory usage beats 10.17 % of python3 submissions (14.7 MB)
# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]
# @lc code=end