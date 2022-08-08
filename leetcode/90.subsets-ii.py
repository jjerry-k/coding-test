#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
# Your runtime beats 16.01 % of python3 submissions
# Your memory usage beats 51.08 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        result = [[]]
        for n in range(1, len(nums)+1):
            for combi in combinations(nums, n):
                combi = sorted(list(combi))
                if combi in result: continue
                result.append(combi)
        return result
# @lc code=end