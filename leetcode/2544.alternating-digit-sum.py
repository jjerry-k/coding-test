#
# @lc app=leetcode id=2544 lang=python3
#
# [2544] Alternating Digit Sum
# Your runtime beats 80.65 % of python3 submissions
# Your memory usage beats 95.72 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum(int(s) * (-2*(idx%2) + 1) for idx, s in enumerate(str(n)))
# @lc code=end