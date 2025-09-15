#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#
from typing import List
# @lc code=start
from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dcount = defaultdict(int)
        dfirst = defaultdict(int)
        dlen   = defaultdict(int) 
        dcount_max = 0
        for (idx,num) in enumerate(nums):
            dcount[num] += 1
            if dcount[num] > dcount_max:
                dcount_max = dcount[num]
            if num not in dfirst:
                dfirst[num] = idx
            else :
                dlen[num] = idx-dfirst[num]+1
        if dcount_max == 1 : 
            return 1  
        return min(dlen[num] for (num, freq ) in dcount.items() if freq == dcount_max)

        
# @lc code=end

nums = [1,2,2,3,1]
print(Solution().findShortestSubArray(nums))