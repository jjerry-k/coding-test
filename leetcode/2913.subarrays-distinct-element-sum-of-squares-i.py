#
# @lc app=leetcode id=2913 lang=python3
#
# [2913] Subarrays Distinct Element Sum of Squares I
# 707/707 cases passed (11 ms)
# Your runtime beats 99.66 % of python3 submissions
# Your memory usage beats 11.5 % of python3 submissions (17.5 MB)
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            distinct = set()
            for j in range(i, n):
                distinct.add(nums[j])
                result += len(distinct) **2
        return result
# @lc code=end