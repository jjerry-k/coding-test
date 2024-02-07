#
# @lc app=leetcode id=2923 lang=python3
#
# [2923] Find Champion I
# Your runtime beats 48.2 % of python3 submissions
# Your memory usage beats 79.21 % of python3 submissions (16.9 MB)
# @lc code=start
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        stronger = [sum(grid[j][i] for j in range(n)) for i in range(n)]
        return stronger.index(min(stronger))
# @lc code=end