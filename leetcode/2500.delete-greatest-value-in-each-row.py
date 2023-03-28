#
# @lc app=leetcode id=2500 lang=python3
#
# [2500] Delete Greatest Value in Each Row
# Your runtime beats 72.8 % of python3 submissions
# Your memory usage beats 49.31 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        for i in range(m):
            grid[i].sort()
        n = len(grid[0])
        return sum(max(grid[j][i] for j in range(m)) for i in range(n))
# @lc code=end