#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#
from typing import List
# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums : 
            return [[lower,upper]]
        missing = []
        for x in nums:
            if lower < x:
                missing.append([lower,x-1])
            lower = x + 1
        if upper > nums[-1]:
            missing.append([x+1,upper])

        return missing


# @lc code=end

