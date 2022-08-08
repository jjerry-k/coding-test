#
# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
# Your runtime beats 50 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (19.3 MB)
# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx, minimum = -1, 10000
        for i, point in enumerate(points):
            if (x-point[0]) * (y-point[1]) != 0: continue
            diff = abs(x - point[0]) + abs(y - point[1])
            if diff < minimum:
                minimum, idx = diff, i
        return idx
# @lc code=end