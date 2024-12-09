#
# @lc app=leetcode id=3079 lang=python3
#
# [3079] Find the Sum of Encrypted Integers
# 865/865 cases passed (45 ms)
# Your runtime beats 90.46 % of python3 submissions
# Your memory usage beats 5.79 % of python3 submissions (17.4 MB)
# @lc code=start
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(num):        
            str_num = str(num)
            max_digit = max(str_num)            
            return int(max_digit * len(str_num))
        return sum(encrypt(num) for num in nums)

# @lc code=en