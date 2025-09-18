#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
from typing import List
# @lc code=start

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        idx = 1
        nums = list(dict.fromkeys(nums).keys())
        nlen = len(nums)
        if nlen == 1:
            return True 
        while nums[idx] <nums[idx-1] and idx < nlen:
            idx +=1 
        if idx == nlen : 
            return True 
        if idx != 1 :
            return False 
        while nums[idx] > nums[idx-1] and idx < nlen:
            idx +=1
        return idx==nlen
        
        

# @lc code=end

nums = [1,2,2,3]
print(Solution().isMonotonic(nums))