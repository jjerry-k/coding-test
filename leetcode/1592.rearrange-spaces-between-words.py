#
# @lc app=leetcode id=1592 lang=python3
#
# [1592] Rearrange Spaces Between Words
# Your runtime beats 82.85 % of python3 submissions
# Your memory usage beats 51 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        split_text = text.split()
        num_blink = text.count(" ")
        if len(split_text) == 1: return split_text[0] + (' ' * num_blink)
        main_spaces, extra_spaces = divmod(num_blink, len(split_text)-1)
        return (" " * main_spaces).join(split_text) + " " * extra_spaces
# @lc code=end