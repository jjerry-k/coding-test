#
# @lc app=leetcode id=1967 lang=python3
#
# [1967] Number of Strings That Appear as Substrings in Word
# Your runtime beats 79.45 % of python3 submissions
# Your memory usage beats 42.37 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0
        for pattern in patterns:
            if pattern in word:
                result += 1
        return result
# @lc code=end