#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
# Your runtime beats 66.1 % of python3 submissions
# Your memory usage beats 90.08 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
# @lc code=end