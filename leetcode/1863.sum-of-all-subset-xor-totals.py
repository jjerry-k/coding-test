#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
# Your runtime beats 35.75 % of python3 submissions
# Your memory usage beats 93.84 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        import itertools, functools
        result = 0
        for num_elem in range(1, len(nums)+1):
            for sub_list in itertools.combinations(nums, num_elem):
                result += functools.reduce(lambda x, y: x ^ y, list(sub_list))
        return result
# @lc code=end