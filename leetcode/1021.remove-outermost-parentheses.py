#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result, open_condition = "", 0
        for char in S:
            if char == "(" and open_condition > 0: result += char
            if char == ")" and open_condition > 1: result += char
            open_condition += 1 if char == "(" else -1
        return result
# @lc code=end