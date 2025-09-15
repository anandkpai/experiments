#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
from heapq import nlargest
from typing import List 
# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return None
        numSet = set(nums)
        if len(numSet) < 3:
            return max(numSet)
        
        return nlargest(3,numSet)[-1]
        
        
        
# @lc code=end

