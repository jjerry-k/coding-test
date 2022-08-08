#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
# Your runtime beats 50 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (20.4 MB)
# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result = 0
        item_key = {"type":0, "color": 1, "name":2}
        for item in items:
            if item[item_key[ruleKey]] == ruleValue: result +=1
        return result
# @lc code=end