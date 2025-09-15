#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
from typing import List 
# @lc code=start
from heapq import nlargest
from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._scache = SortedList(nlargest(k,nums),key=lambda x:-x)  
        self.k = k


    def add(self, val: int) -> int:
        if not self._scache or len(self._scache)<self.k or val > self._scache[-1]:
            self._scache.add(val)
            if len(self._scache)>self.k:
                self._scache.pop()
        return self._scache[-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

klargest = KthLargest(1,[])
print(klargest.add(-3))
print(klargest.add(-2))
print(klargest.add(-4))
print(klargest.add(0))
print(klargest.add(4))
