#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
# Your runtime beats 85.09 % of python3 submissions
# Your memory usage beats 16.04 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: 
            return [0]
        else:
            leftSum = 0
            rightSum = sum(nums[1:])
            result = [leftSum+rightSum]
            for i in range(len(nums)-1):
                leftSum += nums[i]
                rightSum -= nums[i+1]
                result.append(abs(leftSum - rightSum))
            return result
# @lc code=end