#
# @lc app=leetcode id=2194 lang=python3
#
# [2194] Cells in a Range on an Excel Sheet
# Your runtime beats 88.32 % of python3 submissions
# Your memory usage beats 72.35 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []
        start, end = s.split(":")
        col1, row1 = ord(start[0]), int(start[1])
        col2, row2 = ord(end[0])+1, int(end[1])+1

        for col in range(col1, col2):
            for row in range(row1, row2):
                result.append(f"{chr(col)}{row}")

        return result
# @lc code=end