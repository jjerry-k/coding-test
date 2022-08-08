#
# @lc app=leetcode id=2042 lang=python3
#
# [2042] Check if Numbers Are Ascending in a Sentence
# Your runtime beats 90.94 % of python3 submissions
# Your memory usage beats 99.07 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(i) for i in s.split(" ") if i.isdigit()]
        return all([i<j for i, j in zip(nums[:-1], nums[1:])])
# @lc code=end