#
# @lc app=leetcode id=2283 lang=python3
#
# [2283] Check if Number Has Equal Digit Count and Digit Value
# Your runtime beats 31.37 % of python3 submissions
# Your memory usage beats 58.49 % of python3 submissions (16.6 MB)
# @lc code=start
class Solution:
    def digitCount(self, num: str) -> bool:
        return all(num.count(str(i)) == int(num[i]) for i in range(len(num)))
# @lc code=end