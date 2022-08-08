#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
# Your runtime beats 13.56 % of python3 submissions
# Your memory usage beats 41.33 % of python3 submissions (14.5 MB)
# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 0
        for i in range(1, 2001):
            if i in arr: continue
            else:
                num +=1
            if num == k:
                return i
# @lc code=end