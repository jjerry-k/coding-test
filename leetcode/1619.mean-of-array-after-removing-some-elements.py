#
# @lc app=leetcode id=1619 lang=python3
#
# [1619] Mean of Array After Removing Some Elements
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 68.42 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        return sum(sorted(arr)[n // 20 : -n // 20]) / (n * 9 // 10)
# @lc code=end