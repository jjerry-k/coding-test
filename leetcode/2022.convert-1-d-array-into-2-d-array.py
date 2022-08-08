#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
# Your runtime beats 88.45 % of python3 submissions
# Your memory usage beats 88.77 % of python3 submissions (21.4 MB)
# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        num_element = len(original)
        if num_element != m*n: return []
        return [original[i:i+n] for i in range(0, num_element, n)]
# @lc code=end