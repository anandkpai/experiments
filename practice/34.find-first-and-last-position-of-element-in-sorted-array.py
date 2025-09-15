#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

from bisect import bisect_left
from typing import List

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        leftpos = bisect_left(nums, target)
        if leftpos == len(nums) or nums[leftpos] != target:
            return [-1,-1]
        rghtpos = leftpos +1
        while rghtpos < len(nums) and nums[rghtpos] == target:
            rghtpos +=1 
        return [leftpos, rghtpos-1]
        
# @lc code=end

