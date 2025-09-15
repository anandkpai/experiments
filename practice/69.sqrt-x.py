#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: 
            return 1 
        for n in range(1,x//2+2):
            if n*n > x: break 
        return n-1 
            

        
# @lc code=end

