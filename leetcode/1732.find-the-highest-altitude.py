#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
# Your runtime beats 24.67 % of python3 submissions
# Your memory usage beats 88.92 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum, top = 0, 0
        for val in gain: 
            sum += val
            if sum > top: top = sum
        return top
        
# @lc code=end