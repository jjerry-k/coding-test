#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
# Your runtime beats 77.53 % of python3 submissions
# Your memory usage beats 48.42 % of python3 submissions (23.8 MB)
# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        cnt = 0
        for a, b in dominoes:
            key = min(a, b) * 10 + max(a, b) 
            if key in d:
                cnt += d[key]
                d[key] += 1
            else:
                d[key] = 1   
        return cnt
# @lc code=end

