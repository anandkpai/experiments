#
# @lc app=leetcode id=760 lang=python3
#
# [760] Find Anagram Mappings
#
from typing import List
# @lc code=start
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dnums2 = {el:idx for idx,el in enumerate(nums2)}
        return [dnums2[num] for num in nums1]
# @lc code=end

