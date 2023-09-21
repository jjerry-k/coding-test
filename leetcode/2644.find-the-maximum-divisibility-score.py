#
# @lc app=leetcode id=2644 lang=python3
#
# [2644] Find the Maximum Divisibility Score
# Your runtime beats 19.73 % of python3 submissions
# Your memory usage beats 74.71 % of python3 submissions (16.5 MB)
# @lc code=start
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        return -max([sum(n % d == 0 for n in nums), -d] for d in divisors)[1]
# @lc code=end