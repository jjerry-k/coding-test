#
# @lc app=leetcode id=1984 lang=python3
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
# Your runtime beats 14.9 % of python3 submissions
# Your memory usage beats 87.02 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        arr = nums[:k]
        res = arr[-1] - arr[0]
        
        for i in range(k, len(nums)):
            arr.pop(0)
            arr.append(nums[i])
            res = min(res, arr[-1] - arr[0])
            
        return res
# @lc code=end