#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
# Your runtime beats 48.94 % of python3 submissions
# Your memory usage beats 73.97 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b): return False
        if a == b and len(set(a)) < len(a): return True
        dif = [(a_c, b_c) for a_c, b_c in zip(a, b) if a_c != b_c]
        return len(dif) == 2 and dif[0] == dif[1][::-1]
# @lc code=end