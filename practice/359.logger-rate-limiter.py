#
# @lc app=leetcode id=359 lang=python3
#
# [359] Logger Rate Limiter
#
from collections import defaultdict
# @lc code=start
class Logger:

    def __init__(self):
        self._d = defaultdict(lambda : -10000)


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp - self._d[message] >= 10 :
            self._d[message] = timestamp
            return True
        return False 



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
# @lc code=end

