#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
from typing import List


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for idx,val in enumerate(nums):
            if val in d:
                if idx - d[val] <= k: 
                    return True 
            d[val]=idx 
        return False 
# @lc code=end

