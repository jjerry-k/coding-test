#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
# Your runtime beats 59.1 % of python3 submissions
# Your memory usage beats 73.68 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        for i, c in enumerate(s):
            if c.isalpha(): result += c
            else: result += chr(ord(s[i-1]) + int(c))
        return result
# @lc code=end

