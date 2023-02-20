#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
# Your runtime beats 64.36 % of python3 submissions
# Your memory usage beats 53.87 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        nums2 = list(map(int, "".join(list(map(str, nums)))))
        return abs(sum(nums)-sum(nums2))
# @lc code=end