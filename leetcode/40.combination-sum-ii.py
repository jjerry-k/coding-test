#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from itertools import combinations
        candidates = set(candidates)
        result = []
        for i in range(1, len(candidates)+1):
            for combi in combinations(candidates, i):
                if sum(combi) == target:
                    result.append(list(combi))
        return result
# @lc code=end