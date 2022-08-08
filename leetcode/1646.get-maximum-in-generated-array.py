#
# @lc app=leetcode id=1646 lang=python3
#
# [1646] Get Maximum in Generated Array
# Your runtime beats 85.17 % of python3 submissions
# Your memory usage beats 50.31 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2: return n
        nums = [0, 1]
        for i in range(2, n+1):
            if i%2==0:
                nums += [nums[i//2]]
            else:
                nums += [nums[i//2] + nums[(i//2)+1]]
        return max(nums)
# @lc code=end