#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#
from typing import List 
from math import sqrt
# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqRtf = sqrt(area)
        sqRt = int(sqRtf) 
        if sqRt == sqRtf:
            return [sqRt,sqRt]
        x = area
        for i in range(sqRt, 1, -1):
            if not area%i:
                x = i 
                break 
        
        y = area//x
        return [x,y] if x>y else [y,x]

# @lc code=end

print(Solution().constructRectangle(122122))