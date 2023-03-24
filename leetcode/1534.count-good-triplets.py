#
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
# Your runtime beats 20.78 % of python3 submissions
# Your memory usage beats 79.87 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        from itertools import combinations
        result = 0
        for triplet in combinations(arr, 3):
            cond_a = abs(triplet[0] - triplet[1]) <= a
            cond_b = abs(triplet[1] - triplet[2]) <= b
            cond_c = abs(triplet[0] - triplet[2]) <= c
            if  cond_a and cond_b and cond_c:
                result += 1 
        return result
# @lc code=end