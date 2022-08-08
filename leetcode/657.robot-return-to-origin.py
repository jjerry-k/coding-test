#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
# Your runtime beats 90.63 % of python3 submissions
# Your memory usage beats 92.87 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
# @lc code=end