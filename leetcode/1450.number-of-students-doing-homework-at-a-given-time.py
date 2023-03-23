#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
# Your runtime beats 65.11 % of python3 submissions
# Your memory usage beats 60.43 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum((start <= queryTime) and (end >= queryTime) for start, end in zip(startTime, endTime))
# @lc code=end