#
# @lc app=leetcode id=2032 lang=python3
#
# [2032] Two Out of Three
# Your runtime beats 6.75 % of python3 submissions
# Your memory usage beats 85.73 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)        
        return  (nums1 & nums2) | (nums2 & nums3) | (nums3 & nums1)  
# @lc code=end