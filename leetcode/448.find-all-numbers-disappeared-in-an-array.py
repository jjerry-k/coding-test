#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
# Your runtime beats 68.22 % of python3 submissions
# Your memory usage beats 16.71 % of python3 submissions (29 MB)
# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)).difference(set(nums)))
# @lc code=end