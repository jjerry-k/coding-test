#
# @lc app=leetcode id=1816 lang=python3
#
# [1816] Truncate Sentence
# Your runtime beats 59.85 % of python3 submissions
# Your memory usage beats 77.54 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])
# @lc code=end