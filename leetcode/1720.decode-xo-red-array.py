#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
# Your runtime beats 92.56 % of python3 submissions
# Your memory usage beats 64.84 % of python3 submissions (15.8 MB)
# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for a in encoded:
            result.append(result[-1] ^ a)
        return result
# @lc code=end