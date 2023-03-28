#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
# Your runtime beats 44.01 % of python3 submissions
# Your memory usage beats 11.53 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return "111" in "".join(str(num%2) for num in arr)
# @lc code=end