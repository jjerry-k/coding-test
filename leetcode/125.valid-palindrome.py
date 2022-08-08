#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
# Your runtime beats 12.33 % of python3 submissions
# Your memory usage beats 62.86 % of python3 submissions (14.7 MB)
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward, backward = "", ""
        for i in range(len(s)):
            forward += s[i].lower() if s[i].isalnum() else ""
            backward += s[-i-1].lower() if s[-i-1].isalnum()  else ""
        return forward == backward
# @lc code=end