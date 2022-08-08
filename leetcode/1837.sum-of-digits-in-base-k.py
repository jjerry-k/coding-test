#
# @lc app=leetcode id=1837 lang=python3
#
# [1837] Sum of Digits in Base K
# Your runtime beats 81.5 % of python3 submissions
# Your memory usage beats 9.93 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        rev_base = 0
        while n > 0:
            n, mod = divmod(n, k)
            rev_base += mod
        return rev_base 
# @lc code=end