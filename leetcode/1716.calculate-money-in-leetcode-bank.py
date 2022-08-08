#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
# Your runtime beats 82.07 % of python3 submissions
# Your memory usage beats 90.51 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        quotient, remainder = divmod(n, 7)
        return sum(sum(j+i for j in range(1, 8)) for i in range(quotient)) + sum(i+1+quotient for i in range(remainder))
# @lc code=end