#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
# Your runtime beats 13.8 % of python3 submissions
# Your memory usage beats 92 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        out = [None]*len(s)
        for w in s:
            out[int(w[-1])-1] = w[:-1]
        return " ".join(out)

# @lc code=end