#
# @lc app=leetcode id=2928 lang=python3
#
# [2928] Distribute Candies Among Children I
# Your runtime beats 82.37 % of python3 submissions
# Your memory usage beats 69.11 % of python3 submissions (16.5 MB)
# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for i in range(min(n, limit) + 1):
            for j in range(min(n - i, limit) + 1):
                k = n - i - j
                if 0 <= k <= limit:
                    count += 1
        return count
# @lc code=end