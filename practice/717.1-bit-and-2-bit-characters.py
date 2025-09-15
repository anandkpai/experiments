#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#
from typing import List
# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
        if bits[-2] == 0:
            return True
        if len(bits)%2 : 
            return True
        return False 
        
# @lc code=end

