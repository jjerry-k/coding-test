#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
# Your runtime beats 63.34 % of python3 submissions
# Your memory usage beats 79.39 % of python3 submissions (23.1 MB)
# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count("1") for i in range(n+1)]
# @lc code=end