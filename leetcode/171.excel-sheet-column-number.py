#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
# Your runtime beats 21.47 % of python3 submissions
# Your memory usage beats 71.17 % of python3 submissions (16.4 MB)
# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum((ord(en) - 64) * 26**i for i, en in enumerate(columnTitle[::-1]))
# @lc code=end