#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
# Your runtime beats 69.51 % of python3 submissions
# Your memory usage beats 90.05 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter 
        tmp_dict = Counter(arr)
        return len(tmp_dict.values()) == len(set(tmp_dict.values()))  
# @lc code=end