#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
# Your runtime beats 55.59 % of python3 submissions
# Your memory usage beats 98.09 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, num in enumerate(sorted(nums)) if num==target]
# @lc code=end