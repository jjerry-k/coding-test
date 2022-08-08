#
# @lc app=leetcode id=1961 lang=python3
#
# [1961] Check If String Is a Prefix of Array
# Your runtime beats 91.6 % of python3 submissions
# Your memory usage beats 27.3 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        for word in words:
            prefix += word
            if s == prefix:
                return True
        return False
# @lc code=end