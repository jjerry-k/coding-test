#
# @lc app=leetcode id=2133 lang=python3
#
# [2133] Check if Every Row and Column Contains All Numbers
# Your runtime beats 25.93 % of python3 submissions
# Your memory usage beats 24.78 % of python3 submissions (14.5 MB)
# @lc code=start
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        set_ = set(range(1,len(matrix)+1))
        return all(set_ == set(x) for x in matrix+list(zip(*matrix)))
# @lc code=end