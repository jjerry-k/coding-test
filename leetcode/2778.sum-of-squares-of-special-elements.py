#
# @lc app=leetcode id=2778 lang=python3
#
# [2778] Sum of Squares of Special Elements 
# Your runtime beats 39.12 % of python3 submissions
# Your memory usage beats 71.12 % of python3 submissions (16.5 MB)
# @lc code=start
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(nums[i-1]**2 for i in range(1,len(nums)+1) if len(nums)%i==0 )
# @lc code=end