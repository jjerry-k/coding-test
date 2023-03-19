#
# @lc app=leetcode id=2469 lang=python3
#
# [2469] Convert the Temperature
# Your runtime beats 66.11 % of python3 submissions
# Your memory usage beats 39.09 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kalvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        
        return [kalvin, fahrenheit]
# @lc code=end