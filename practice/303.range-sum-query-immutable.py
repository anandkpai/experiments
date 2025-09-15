#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
from typing import List 
# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        cSum = [0]
        for x in nums:
            cSum.append(cSum[-1]+x)
        self.cSum = cSum 

        

    def sumRange(self, left: int, right: int) -> int:
        return  self.cSum[right+1]-self.cSum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

