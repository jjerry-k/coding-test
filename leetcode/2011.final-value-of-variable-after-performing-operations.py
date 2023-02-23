#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
# Your runtime beats 28.94 % of python3 submissions
# Your memory usage beats 94.26 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if ops[1]=="+" else -1 for ops in operations)
# @lc code=end

