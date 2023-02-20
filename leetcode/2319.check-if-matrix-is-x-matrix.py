#
# @lc app=leetcode id=2319 lang=python3
#
# [2319] Check if Matrix Is X-Matrix
# Your runtime beats 54.73 % of python3 submissions
# Your memory usage beats 18.24 % of python3 submissions (15 MB)
# @lc code=start
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            l_idx = i
            r_idx = n-1-i
            for j in range(n):
                if (j in [l_idx, r_idx]) and (grid[i][j] == 0):
                    return False
                elif (j not in [l_idx, r_idx]) and (grid[i][j] != 0):
                    return False
        return True

# @lc code=end