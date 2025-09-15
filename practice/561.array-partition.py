#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#
from typing import List 
# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
# @lc code=end

