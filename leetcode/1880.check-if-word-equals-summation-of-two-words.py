#
# @lc app=leetcode id=1880 lang=python3
#
# [1880] Check if Word Equals Summation of Two Words
# Your runtime beats 82.78 % of python3 submissions
# Your memory usage beats 24.06 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        FW = int("".join(str(ord(i)-97) for i in firstWord))
        SW = int("".join(str(ord(i)-97) for i in secondWord))
        TW = int("".join(str(ord(i)-97) for i in targetWord))
        return (FW + SW) == TW
# @lc code=end

