#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
# Your runtime beats 86.79 % of python3 submissions
# Your memory usage beats 26.42 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0, len(s), k):
            word_length = len(s[i:i+k])
            if word_length < k:
                result.append(s[i:i+k] + fill*(k-word_length))
            else:
                result.append(s[i:i+k])
        return result
# @lc code=end