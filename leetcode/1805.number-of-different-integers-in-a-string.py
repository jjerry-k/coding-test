#
# @lc app=leetcode id=1805 lang=python3
#
# [1805] Number of Different Integers in a String
# Your runtime beats 99.35 % of python3 submissions
# Your memory usage beats 59.27 % of python3 submissions (14.3 MB)
# @lc code=start
# %%
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ''.join(c if c.isdigit() else ' ' for c in word)
        return len(set(map(int, s.split())))
# @lc code=end