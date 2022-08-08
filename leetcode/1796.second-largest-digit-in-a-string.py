#
# @lc app=leetcode id=1796 lang=python3
#
# [1796] Second Largest Digit in a String
# Your runtime beats 91.4 % of python3 submissions
# Your memory usage beats 20.8 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        s = set(s)
        digits = []
        for val in s:
            if val.isdigit(): 
                digits.append(int(val))
        return sorted(digits)[-2] if len(digits) > 1 else -1
# @lc code=end