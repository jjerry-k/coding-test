#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
# Your runtime beats 81.41 % of python3 submissions
# Your memory usage beats 27.75 % of python3 submissions (14.5 MB)
# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list(map(int, "".join(list(map(str, nums)))))
# @lc code=end