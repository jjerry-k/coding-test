#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
# Your runtime beats 16.38 % of python3 submissions
# Your memory usage beats 13.96 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: 
            return word
        else:
            end_idx = word.index(ch) + 1
            return word[:end_idx][::-1] + word[end_idx:]
# @lc code=end