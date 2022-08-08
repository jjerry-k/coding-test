#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
# Your runtime beats 49.03 % of python3 submissions
# Your memory usage beats 48.3 % of python3 submissions (14.8 MB)
# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        return all((y2 - y1) * (x - x1) == (y - y1) * (x2 - x1) for x, y in coordinates[2:])
# @lc code=end