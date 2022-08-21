#
# @lc app=leetcode id=2325 lang=python3
#
# [2325] Decode the Message
# Your runtime beats 93.98 % of python3 submissions
# Your memory usage beats 36.17 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode = {" ": " "}
        i = 0
        for k in key:
            if k in decode or k == " ": continue
            if len(decode) == 27: break
            decode[k] = chr(ord("a") + i)
            i += 1
        
        result = ""
        for m in message:
            result += decode[m]
        return result
# @lc code=end