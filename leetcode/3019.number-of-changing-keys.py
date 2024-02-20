#
# @lc app=leetcode id=3019 lang=python3
#
# [3019] Number of Changing Keys
# Your runtime beats 97.84 % of python3 submissions
# Your memory usage beats 91.08 % of python3 submissions (16.5 MB)
# @lc code=start
class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum([s[i].lower() != s[i+1].lower() for i in range(len(s)-1)])
# @lc code=end

