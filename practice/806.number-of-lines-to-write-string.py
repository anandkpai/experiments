#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#
from typing import List
# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        pixCount = 0 
        lineCount = 0 
        base = ord('a')
        for c in s:
            idx = ord(c)-base
            w = widths[idx]
            if pixCount + w > 100:
                pixCount = w
                lineCount += 1
            else : 
                pixCount += w

        return [lineCount+1, pixCount] 
# @lc code=end

