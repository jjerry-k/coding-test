#
# @lc app=leetcode id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
# Your runtime beats 99.47 % of python3 submissions
# Your memory usage beats 45.82 % of python3 submissions (14.8 MB)
# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result = 0
        for box, unit in sorted(boxTypes, key=lambda x: x[1], reverse =True):
            if truckSize == 0: break
            elif truckSize >= box:
                result += box*unit
                truckSize -= box
            else: 
                result += truckSize*unit
                truckSize = 0
        return result

# @lc code=end