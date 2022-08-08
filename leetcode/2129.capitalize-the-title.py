#
# @lc app=leetcode id=2129 lang=python3
#
# [2129] Capitalize the Title
# Your runtime beats 35.61 % of python3 submissions
# Your memory usage beats 15 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([word.capitalize() if len(word) > 2 else word.lower() for word in title.split(" ")])
# @lc code=end