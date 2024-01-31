#
# @lc app=leetcode id=2946 lang=python3
#
# [2946] Matrix Similarity After Cyclic Shifts
# Your runtime beats 72.63 % of python3 submissions
# Your memory usage beats 43.66 % of python3 submissions (16.5 MB)
# @lc code=start
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k = k % len(mat[0])
        if not k : return True
        else:
            return all(row == row[k:]+row[:k] for row in mat)     
# @lc code=end