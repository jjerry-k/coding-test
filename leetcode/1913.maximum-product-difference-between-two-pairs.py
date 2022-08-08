#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
# Your runtime beats 63.85 % of python3 submissions
# Your memory usage beats 79.73 % of python3 submissions (15.3 MB)
# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[-1]*nums[-2] - nums[0]*nums[1]
# @lc code=end