#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
# Your runtime beats 68.94 % of python3 submissions
# Your memory usage beats 34.74 % of python3 submissions (14.5 MB)
# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        cnt = sum([1 for num in nums if num < 0])%2
        return 1 if cnt == 0 else -1
# @lc code=end

