#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
# Your runtime beats 97.76 % of python3 submissions
# Your memory usage beats 36.25 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char): return False
        return True
# @lc code=end