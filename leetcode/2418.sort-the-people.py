#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
# Your runtime beats 46.43 % of python3 submissions
# Your memory usage beats 78.64 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=zip(heights,names)
        l=[]
        for i,j in sorted(a):
            l.append(j)
        return l[::-1]
# @lc code=end