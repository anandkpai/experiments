#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#
from typing import List
# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evnIdx = 0 
        oddIdx = 1
        while evnIdx < len(nums)-1 and oddIdx < len(nums):
            while nums[evnIdx]%2 == 0: 
                evnIdx += 2
            while nums[oddIdx]%2 == 1: 
                oddIdx += 2
            if evnIdx < len(nums)-1 and oddIdx < len(nums):
                nums[evnIdx], nums[oddIdx] = nums[oddIdx], nums[evnIdx]
                evnIdx +=2
                oddIdx +=2

        return nums
        
# @lc code=end

