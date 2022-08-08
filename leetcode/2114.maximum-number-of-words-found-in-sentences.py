#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
# Your runtime beats 84.49 % of python3 submissions
# Your memory usage beats 7.84 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split(" ")) for sentence in sentences)
# @lc code=end