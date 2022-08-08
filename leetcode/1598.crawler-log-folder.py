#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
# Your runtime beats 57.11 % of python3 submissions
# Your memory usage beats 81.59 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for log in logs:
            if log == "../":
                cnt -= 1
                cnt = max(0, cnt)
            elif log == "./": continue
            else: cnt += 1
        return cnt
# @lc code=end