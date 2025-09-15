#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#
from typing import List 
# @lc code=start
from heapq import nlargest, nsmallest
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest = nlargest(3,nums)
        smllest = nsmallest(2,nums)
        default = largest[0]*largest[1]*largest[2]
        if largest[0]>0 and smllest[0] < 0 : 
            return max(default, smllest[0]*smllest[1]*largest[0])
        return default 


# @lc code=end

