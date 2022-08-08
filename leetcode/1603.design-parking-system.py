#
# @lc app=leetcode id=1603 lang=python3
#
# [1603] Design Parking System
# Your runtime beats 92.72 % of python3 submissions
# Your memory usage beats 54.77 % of python3 submissions (14.8 MB)
# @lc code=start
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cnt = {
            1: big, 
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        if not self.cnt[carType]: return False
        else:
            self.cnt[carType] -= 1
            return True
# @lc code=end