#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        common = []
        for num in d1:
            if num in d2 :
                common.extend(min(d1[num],d2[num])*[num])
        return common 
        
# @lc code=end

