#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
from typing import List 
# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1.union(set2)-(set1-set2)-(set2-set1))
        
# @lc code=end

