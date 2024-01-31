#
# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
# Your runtime beats 11.99 % of python3 submissions
# Your memory usage beats 66.07 % of python3 submissions (17.8 MB)
# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x = ""
        result = []
        for num in nums:
            x += str(num)
            result.append((int(x, 2) % 5)==0)
        return result
# @lc code=end