#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#
from typing import List
# @lc code=start
from heapq import nlargest
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums_with_index = [(y,x) for x,y in enumerate(nums)]
        highest, nexthighest = nlargest(2,nums_with_index)
        return highest[1] if highest[0] >= 2*nexthighest[0] else -1 
        
# @lc code=end

nums = [1,2,3,4]


print(Solution().dominantIndex(nums))