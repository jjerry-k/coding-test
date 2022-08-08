#
# @lc app=leetcode id=2124 lang=python3
#
# [2124] Check if All A's Appears Before All B's
# Your runtime beats 17.14 % of python3 submissions
# Your memory usage beats 9.65 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        return s == "".join(sorted(s))
# @lc code=end