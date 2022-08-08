#
# @lc app=leetcode id=2185 lang=python3
#
# [2185] Counting Words With a Given Prefix
# Your runtime beats 66.83 % of python3 submissions
# Your memory usage beats 97.23 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(True if word[:len(pref)] == pref else False for word in words)
# @lc code=end