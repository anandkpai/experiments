#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
from typing import List
# @lc code=start
from heapq import heapify, heappop, heappush
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # by using a heap queue, we can build the next value for each 
        # element in a single pass     
        numsheap = []
        heapify(numsheap)
        dgt = dict()
        for val in nums2:
            while numsheap and val > numsheap[0]:
                dgt[heappop(numsheap)] = val
            heappush(numsheap,val)

        return  [dgt[n1] if n1 in dgt else -1 for n1 in nums1]
        

# @lc code=end

nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(Solution().nextGreaterElement(nums1,nums2))