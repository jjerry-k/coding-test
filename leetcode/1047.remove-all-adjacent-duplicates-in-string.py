#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
# Your runtime beats 79.01 % of python3 submissions
# Your memory usage beats 39.03 % of python3 submissions (14.7 MB)
# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)
# @lc code=end