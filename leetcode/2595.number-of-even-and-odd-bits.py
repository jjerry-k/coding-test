#
# @lc app=leetcode id=2595 lang=python3
#
# [2595] Number of Even and Odd Bits
# Your runtime beats 6.91 % of python3 submissions
# Your memory usage beats 94.27 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        result = [0, 0]
        n = format(n, "b")[::-1]
        for i, tmp in enumerate(n):
            if tmp == "1":
                result[i%2] +=1
        return result
# @lc code=end