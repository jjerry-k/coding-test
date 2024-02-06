#
# @lc app=leetcode id=2744 lang=python3
#
# [2744] Find Maximum Number of String Pairs
# Your runtime beats 96.09 % of python3 submissions
# Your memory usage beats 75.88 % of python3 submissions (16.5 MB)
# @lc code=start
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        return len(words) - len(set(''.join(sorted(word)) for word in words))
# @lc code=end