#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
from typing import List
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nsum = sum(nums)
        csum = 0
        for idx, val in enumerate(nums):            
            if csum == (nsum-val)/2:
                return idx 
            csum += val 
        return -1                

        
# @lc code=end

