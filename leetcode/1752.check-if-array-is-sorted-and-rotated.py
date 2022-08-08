#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
# Your runtime beats 51.3 % of python3 submissions
# Your memory usage beats 44.14 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return nums[i:] + nums[:i] == sorted(nums)
        return True
# @lc code=end