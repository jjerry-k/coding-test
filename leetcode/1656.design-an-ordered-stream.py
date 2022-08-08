#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
# Your runtime beats 7.43 % of python3 submissions
# Your memory usage beats 58.94 % of python3 submissions (15.1 MB)
# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.stream = [None] * (n+2)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if idKey == self.ptr:
            while self.stream[self.ptr] is not None:
                self.ptr += 1
        return self.stream[idKey:self.ptr]
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end