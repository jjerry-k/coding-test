#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
# Your runtime beats 33.52 % of python3 submissions
# Your memory usage beats 21.77 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        return all(x % 2 == 0 for x in Counter(nums).values())
# @lc code=end