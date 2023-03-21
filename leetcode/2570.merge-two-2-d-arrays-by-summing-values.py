#
# @lc app=leetcode id=2570 lang=python3
#
# [2570] Merge Two 2D Arrays by Summing Values
# Your runtime beats 99.3 % of python3 submissions
# Your memory usage beats 79.24 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        while nums1 and nums2:
            num1 = nums1[0]
            num2 = nums2[0]
            
            if num1[0] == num2[0]:
                result.append([num1[0], num1[1]+num2[1]])
                nums1.pop(0)
                nums2.pop(0)
            
            elif num1[0] < num2[0]:
                result.append(num1)
                nums1.pop(0)
            
            else:
                result.append(num2)
                nums2.pop(0)
        while nums1: result.append(nums1.pop(0))
        while nums2: result.append(nums2.pop(0))
            
        return result
# @lc code=end