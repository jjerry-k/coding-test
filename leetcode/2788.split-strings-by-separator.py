#
# @lc app=leetcode id=2788 lang=python3
#
# [2788] Split Strings by Separator
# Your runtime beats 78.52 % of python3 submissions
# Your memory usage beats 51.08 % of python3 submissions (16.7 MB)
# @lc code=start
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            result += [tmp for tmp in word.split(separator) if tmp]
        return result
# @lc code=end