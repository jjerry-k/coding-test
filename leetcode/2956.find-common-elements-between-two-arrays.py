#
# @lc app=leetcode id=2956 lang=python3
#
# [2956] Find Common Elements Between Two Arrays
# Your runtime beats 43.24 % of python3 submissions
# Your memory usage beats 33.87 % of python3 submissions (16.5 MB)
# @lc code=start
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [sum(num in nums2 for num in nums1), sum(num in nums1 for num in nums2)]
# @lc code=end