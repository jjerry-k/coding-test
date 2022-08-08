#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
# Your runtime beats 57.67 % of python3 submissions
# Your memory usage beats 53.66 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        import itertools
        cnt = 0
        for x, y in itertools.combinations(nums, 2):
            if abs(x-y) == k:
                cnt +=1
        return cnt
# @lc code=end