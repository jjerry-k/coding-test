#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
# Your runtime beats 56.16 % of python3 submissions
# Your memory usage beats 93.07 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        from math import ceil
        num_iter, result = ceil(len(arr)/2), 0
        for i in range(num_iter):
            odd_length = 2*i + 1
            for j in range(len(arr)-odd_length+1):
                result += sum(arr[j:j+odd_length])
        return result
# @lc code=end