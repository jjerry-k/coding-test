#
# @lc app=leetcode id=1945 lang=python3
#
# [1945] Sum of Digits of String After Convert
# Your runtime beats 72.14 % of python3 submissions
# Your memory usage beats 57.71 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:    
        num = ""
        for alpha in s:
            num += str(ord(alpha)-96)
        num = int(num)

        for _ in range(k):
            result = 0
            num = str(num)
            for i in num:
                result += int(i)
            num = result
        return result
        
# @lc code=end