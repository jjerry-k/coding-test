#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
# Your runtime beats 5.02 % of python3 submissions
# Your memory usage beats 61.59 % of python3 submissions (17.6 MB)
# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        for f in firstList:
            for s in secondList:
                    if f[0]<=s[0]<=f[1] or f[0]<=s[1]<=f[1] or s[0]<=f[0]<=s[1] or s[0]<=f[1]<=s[1]:
                        result.append([max(f[0], s[0]), min(f[1], s[1])])
        return result
# @lc code=end