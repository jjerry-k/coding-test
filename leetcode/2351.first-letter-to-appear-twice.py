#
# @lc app=leetcode id=2351 lang=python3
#
# [2351] First Letter to Appear Twice
# Your runtime beats 17.54 % of python3 submissions
# Your memory usage beats 96.16 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        map_dict = {}
        for a in s:
            if a not in map_dict:
                map_dict[a] = 1
            else:
                map_dict[a] += 1
            if map_dict[a] == 2:
                return a

# @lc code=end