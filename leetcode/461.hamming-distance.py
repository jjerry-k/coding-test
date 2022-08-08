#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
# Your runtime beats 96.29 % of python3 submissions
# Your memory usage beats 76.64 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
# @lc code=end