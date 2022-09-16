#
# @lc app=leetcode id=2357 lang=python3
#
# [2357] Make Array Zero by Subtracting Equal Amounts
# Your runtime beats 84.56 % of python3 submissions
# Your memory usage beats 96.67 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})
# @lc code=end