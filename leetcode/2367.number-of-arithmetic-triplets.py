#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
# Your runtime beats 41.67 % of python3 submissions
# Your memory usage beats 66.67 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
                ans += 1
        
        return ans
# @lc code=end