#
# @lc app=leetcode id=3364 lang=python3
#
# [3364] Minimum Positive Sum Subarray 
# Your runtime beats 23.53 % of python3 submissions
# Your memory usage beats 5.99 % of python3 submissions (17.5 MB)
# @lc code=start
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        found = False
        for length in range(l, r + 1):
            for start in range(n - length + 1):
                curr_sum = sum(nums[start:start + length])
                if curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)
                    found = True
        return min_sum if found else -1
# @lc code=end