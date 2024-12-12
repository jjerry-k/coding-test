#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
# 8/8 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 18.83 % of python3 submissions (17.4 MB)
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
    
        def backtrack(open_count: int, close_count: int, current: str):
            if len(current) == 2 * n:
                result.append(current)
                return
            
            if open_count < n:
                backtrack(open_count + 1, close_count, current + "(")
                
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current + ")")
        
        backtrack(0, 0, "")
        return result
# @lc code=end