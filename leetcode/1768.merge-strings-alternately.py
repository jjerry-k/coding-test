#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
# Your runtime beats 66.67 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(c1 + c2 for c1, c2 in zip_longest(word1, word2, fillvalue=''))
# @lc code=end