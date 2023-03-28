#
# @lc app=leetcode id=2586 lang=python3
#
# [2586] Count the Number of Vowel Strings in Range
# Your runtime beats 62.75 % of python3 submissions
# Your memory usage beats 41.02 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        result = 0
        vowels = ["a", "e", "i", "o", "u"]
        for word in words[left:right+1]:
            if (word[0] in vowels) and (word[-1] in vowels):
                result +=1
        return result
# @lc code=end