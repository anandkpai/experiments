#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#
from typing import List 

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ptime = 0 
        endTime = -1
        for t in timeSeries:
            if t > endTime:
                ptime += duration
            else : 
                ptime += t+duration-1 - endTime
            endTime = t+duration-1 
        return ptime 
# @lc code=end

