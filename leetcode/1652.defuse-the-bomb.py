#
# @lc app=leetcode id=1652 lang=python3
#
# [1652] Defuse the Bomb
# Your runtime beats 51.01 % of python3 submissions
# Your memory usage beats 99.6 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        numbers = len(code)
        code = code*3
        if k == 0:
            return [0] * numbers
        elif k > 0:
            return [sum(code[i+j] for j in range(1, k+1)) for i in range(numbers)]
        else : 
            return [sum(code[i+j] for j in range(-1, k-1, -1)) for i in range(numbers)]
# @lc code=end