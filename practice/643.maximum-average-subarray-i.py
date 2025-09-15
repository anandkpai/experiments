#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
from typing import List 
# @lc code=start

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k : 
            return sum(nums)/k
        if k == 1 : return max(nums)
        rsum = maxsum = sum(nums[:k:])
        for idx in range(k,len(nums)):
            rsum   += nums[idx] - nums[idx-k]            
            maxsum  = max(rsum, maxsum)
        return maxsum/k
        
# @lc code=end

nums = [1,12,-5,-6,50,3]
k =4
print(Solution().findMaxAverage(nums,k))
