#
# @lc app=leetcode id=2085 lang=python3
#
# [2085] Count Common Words With One Occurrence
# Your runtime beats 17.2 % of python3 submissions
# Your memory usage beats 83.86 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        union = set(words1).union(set(words2))
        cnt = 0
        for word in union:
            if (words1.count(word) == 1) and (words2.count(word) == 1):
                cnt +=1
        return cnt
# @lc code=end