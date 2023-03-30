#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
# Your runtime beats 59.43 % of python3 submissions
# Your memory usage beats 47.55 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        min_num = min(a,b)
        if max(a,b) % min_num == 0:
            count +=1
        for i in range(1,(min_num//2)+1):
            if a % i == 0 and b % i ==0:
                count +=1
        return count
# @lc code=end

