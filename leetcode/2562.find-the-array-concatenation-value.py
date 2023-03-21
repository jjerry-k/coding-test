#
# @lc app=leetcode id=2562 lang=python3
#
# [2562] Find the Array Concatenation Value
# Your runtime beats 69.64 % of python3 submissions
# Your memory usage beats 72.51 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        num_iters = len(nums) // 2
        for i in range(num_iters):
            l_num = nums[i]
            r_num = nums[-i-1]
            concat = int(str(l_num)+str(r_num))
            result += concat
        if len(nums)%2 == 1:
            result += nums[num_iters]
        
        return result
# @lc code=end