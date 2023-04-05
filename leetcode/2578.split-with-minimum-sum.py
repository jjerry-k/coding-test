#
# @lc app=leetcode id=2578 lang=python3
#
# [2578] Split With Minimum Sum
# Your runtime beats 72.72 % of python3 submissions
# Your memory usage beats 47.09 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def splitNum(self, num: int) -> int:
        num = sorted(list(str(num)))

        num1,num2 = int(''.join(num[0::2])), int(''.join(num[1::2]))
        return num1+num2   
# @lc code=end