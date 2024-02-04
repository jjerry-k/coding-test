#
# @lc app=leetcode id=2169 lang=python3
#
# [2169] Count Operations to Obtain Zero
# Your runtime beats 7.96 % of python3 submissions
# Your memory usage beats 56.44 % of python3 submissions (16.6 MB)
# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            num1, num2 = sorted([num1, num2], reverse=True)
            num1 -= num2
            count +=1
        return count
# @lc code=end