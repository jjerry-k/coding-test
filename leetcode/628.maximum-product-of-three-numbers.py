#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
# Your runtime beats 85.43 % of python3 submissions
# Your memory usage beats 93.52 % of python3 submissions (15.3 MB)
# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
# @lc code=end