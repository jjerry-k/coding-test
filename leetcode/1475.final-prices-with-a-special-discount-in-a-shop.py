#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
# Your runtime beats 73.48 % of python3 submissions
# Your memory usage beats 15.31 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)-1):
            low = True
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    low = False
                    break
            if low:
                result.append(prices[i])
            else:
                result.append(prices[i] - prices[j])
        result.append(prices[-1])
        return result
# @lc code=end