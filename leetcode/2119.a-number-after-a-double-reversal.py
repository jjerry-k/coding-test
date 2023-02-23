#
# @lc app=leetcode id=2119 lang=python3
#
# [2119] A Number After a Double Reversal
# Your runtime beats 26.08 % of python3 submissions
# Your memory usage beats 44.27 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num_str = str(num)
        rev_num_str = num_str[::-1]
        rev_num = int(rev_num_str)
        if str(rev_num)[::-1] == num_str:
            return True
        else: 
            return False 
# @lc code=end

