#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
from typing import List
# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing_number = (set(list((range(1,len(nums)+1))))-set(nums)).pop()
        d= set()
        dupe = None
        for n in nums:
            if n in d:
                dupe = n 
                break 
            d.add(n)

        return [dupe,missing_number]

        
# @lc code=end

