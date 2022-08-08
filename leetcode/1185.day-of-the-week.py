#
# @lc app=leetcode id=1185 lang=python3
#
# [1185] Day of the Week
# Your runtime beats 59.43 % of python3 submissions
# Your memory usage beats 57.73 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        from datetime import date
        return date(year, month, day).strftime("%A")
# @lc code=end