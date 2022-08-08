#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
# Your runtime beats 33.63 % of python3 submissions
# Your memory usage beats 95.93 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        result = [[]]
        for n in range(1, len(nums)+1):
            for combi in combinations(nums, n):
                result.append(list(combi))
        return result
# @lc code=end