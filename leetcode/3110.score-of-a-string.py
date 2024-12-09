#
# @lc app=leetcode id=3110 lang=python3
#
# [3110] Score of a String
# 705/705 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 13.23 % of python3 submissions (17 MB)
# @lc code=start
class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1))
# @lc code=end