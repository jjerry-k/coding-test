#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
# Your runtime beats 61.25 % of python3 submissions
# Your memory usage beats 90.18 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth, cur_depth = 0, 0
        for char in s:
            if char == "(":
                cur_depth += 1
                max_depth = max(max_depth, cur_depth)
            elif char == ")":
                cur_depth -= 1
            else:
                continue
        return max_depth
# @lc code=end