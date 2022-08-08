#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
# Your runtime beats 64.52 % of python3 submissions
# Your memory usage beats 49.66 % of python3 submissions (14.5 MB)
# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum(sum(r[j] for j in {i, len(r) - i - 1}) for i, r in enumerate(mat))
# @lc code=end