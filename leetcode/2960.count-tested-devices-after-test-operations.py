#
# @lc app=leetcode id=2960 lang=python3
#
# [2960] Count Tested Devices After Test Operations
# Your runtime beats 46.15 % of python3 submissions
# Your memory usage beats 22.03 % of python3 submissions (16.5 MB)
# @lc code=start
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        cnt = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                cnt += 1
                for j in range(i+1, len(batteryPercentages)):
                    batteryPercentages[j]-=1
        return cnt
# @lc code=end