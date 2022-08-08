#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
# Your runtime beats 5.07 % of python3 submissions
# Your memory usage beats 6.76 % of python3 submissions (16 MB)
# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return max(set(arr), key=arr.count)
# @lc code=end