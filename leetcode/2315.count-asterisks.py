#
# @lc app=leetcode id=2315 lang=python3
#
# [2315] Count Asterisks
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        between_pairs = False
        for c in s:
            if c == '|':
                between_pairs = not between_pairs
            elif c == '*':
                if not between_pairs:
                    count += 1
        return count
# @lc code=end