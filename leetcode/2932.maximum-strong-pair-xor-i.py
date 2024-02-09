#
# @lc app=leetcode id=2932 lang=python3
#
# [2932] Maximum Strong Pair XOR I
# Your runtime beats 64.37 % of python3 submissions
# Your memory usage beats 66.73 % of python3 submissions (16.5 MB)
# @lc code=start
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_value = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    max_value = max(max_value, nums[i]^nums[j])
        return max_value

# @lc code=end