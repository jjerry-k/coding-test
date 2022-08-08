#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
# Your runtime beats 97.73 % of python3 submissions
# Your memory usage beats 25.88 % of python3 submissions (14.9 MB)
# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        result = []
        for idx in range(0, len_nums, 2):
            freq, val = nums[idx:idx+2]
            result += [val]*freq
        return result
# @lc code=end