#
# @lc app=leetcode id=3005 lang=python3
#
# [3005] Count Elements With Maximum Frequency
# Your runtime beats 96.54 % of python3 submissions
# Your memory usage beats 90.99 % of python3 submissions (16.5 MB)
# @lc code=start
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        maxi=0
        l=[]
        for i in count:
            l.append(count[i])
            maxi=max(maxi,count[i])
        return l.count(maxi)*maxi
# @lc code=end