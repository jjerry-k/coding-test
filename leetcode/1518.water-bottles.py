#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
# Your runtime beats 81.22 % of python3 submissions
# Your memory usage beats 9.64 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1)//(numExchange - 1)
# @lc code=end