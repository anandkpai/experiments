#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#
from typing import List 
# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        required_diff = (sum(aliceSizes)-sum(bobSizes))/2
        setb = set(bobSizes)
        for size in aliceSizes:
            if size-required_diff in setb:
                return size, size-required_diff


# @lc code=end

