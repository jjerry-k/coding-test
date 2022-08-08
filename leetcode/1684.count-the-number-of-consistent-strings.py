#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
# Your runtime beats 23.94 % of python3 submissions
# Your memory usage beats 44.42 % of python3 submissions (16.1 MB)
# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all([char in allowed for char in set(word)]) for word in words)
# @lc code=end