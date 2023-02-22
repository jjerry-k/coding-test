#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
# Your runtime beats 21.45 % of python3 submissions
# Your memory usage beats 51.57 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        
        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
        
        return max(pos, neg)
# @lc code=end