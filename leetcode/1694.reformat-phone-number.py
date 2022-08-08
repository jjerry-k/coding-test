#
# @lc app=leetcode id=1694 lang=python3
#
# [1694] Reformat Phone Number
# Your runtime beats 66.88 % of python3 submissions
# Your memory usage beats 56.2 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = "".join(num for num in number if num.isdigit())
        result = []
        while len(number):
            if len(number) > 4:
                result += [number[:3]]
                number = number[3:]
            elif len(number) == 4:
                result += [number[:2], number[2:]]
                number = ""
            else:
                result += [number]
                number = ""
        return "-".join(result)
# @lc code=end

