#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
from bisect import bisect_left
class RecentCounter:

    def __init__(self):
        self._cache = 1000*[-3000]
        self._idx = 0
        self._hi = 0

    def ping(self, t: int) -> int:
        self._idx = bisect_left(self._cache, t-3000,lo=self._idx, hi = self._hi )
        self._cache[self._idx] = t
        self._hi += 1
        return len(self._cache) - self._idx 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

