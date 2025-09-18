#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
from typing import List
# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        oddIdx = 0 
        evnIdx = len(nums)-1
        while oddIdx < evnIdx :
            while nums[oddIdx]%2==0:
                oddIdx +=1
            while nums[evnIdx]%2 !=0:
                    evnIdx -=1
            nums[oddIdx], nums[evnIdx] = nums[evnIdx], nums[oddIdx]
            oddIdx +=1 
            evnIdx -=1 
        return nums 
        
# @lc code=end

nums = [3,1,2,4]
print(Solution().sortArrayByParity(nums))