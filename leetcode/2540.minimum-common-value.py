#
# @lc app=leetcode id=2540 lang=python3
#
# [2540] Minimum Common Value
# Your runtime beats 88.01 % of python3 submissions
# Your memory usage beats 32.07 % of python3 submissions (39.2 MB)
# @lc code=start
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        result = {}
        nums1.sort()
        nums2.sort()
        for num in nums1:
            result[num] = 1
        
        for num in nums2:
            if num in result and result[num]==1:
                return num
        return -1
# @lc code=end

