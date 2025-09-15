#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#
from typing import List 
# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = 0 
        currentChar = s[0]
        intervals = []
        for idx, ch in enumerate(s):
            if ch != currentChar:
                if idx-start>=3 :
                    intervals.append((start,idx-1))
                start = idx
                currentChar = ch
        return intervals

# @lc code=end

