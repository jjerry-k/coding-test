#
# @lc app=leetcode id=1812 lang=python3
#
# [1812] Determine Color of a Chessboard Square
# Your runtime beats 59.39 % of python3 submissions
# Your memory usage beats 88.61 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) - ord('a') + int(coordinates[1])-1)%2 == 1
# @lc code=end