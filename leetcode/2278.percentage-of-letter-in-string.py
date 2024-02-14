#
# @lc app=leetcode id=2278 lang=python3
#
# [2278] Percentage of Letter in String
# Your runtime beats 43.22 % of python3 submissions
# Your memory usage beats 74.15 % of python3 submissions (16.6 MB)
# @lc code=start
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(s.count(letter)/len(s)*100)
# @lc code=end

