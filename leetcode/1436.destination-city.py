#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
# Your runtime beats 59.49 % of python3 submissions
# Your memory usage beats 32.13 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departure = [path[0] for path in paths]
        arrival = [path[1] for path in paths if path[1] not in departure]
        return arrival[0]
# @lc code=end