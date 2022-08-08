#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
# Your runtime beats 96.38 % of python3 submissions
# Your memory usage beats 64.82 % of python3 submissions (20.6 MB)
# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return sorted(A) in (A, A[::-1])
# @lc code=end