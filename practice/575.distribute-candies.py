#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#
from typing import List 
# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)),len(candyType)//2)
# @lc code=end

