#
# @lc app=leetcode id=2496 lang=python3
#
# [2496] Maximum Value of a String in an Array
# Your runtime beats 50.12 % of python3 submissions
# Your memory usage beats 48.15 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(tmp_str) if tmp_str.isdigit() else len(tmp_str) for tmp_str in strs)
# @lc code=end