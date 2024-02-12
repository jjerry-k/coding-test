#
# @lc app=leetcode id=2965 lang=python3
#
# [2965] Find Missing and Repeated Values
# Your runtime beats 9.36 % of python3 submissions
# Your memory usage beats 32.66 % of python3 submissions (17 MB)
# @lc code=start
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        used_history = []
        result = []
        nums = list(range(1, n**2 + 1))
        for row in grid:
            for i in range(n):
                if row[i] in nums:
                    nums.remove(row[i])
                if row[i] in used_history:
                    result.append(row[i])
                used_history.append(row[i])
        return result + nums
# @lc code=end