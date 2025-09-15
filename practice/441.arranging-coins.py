#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
from math import sqrt
# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # this is actually a famous problem where for a 
        # given number k, you add 1+2+3 .. k 
        # in that case, the sum s = k(k+1)/2
        # hence k^2+k-2n = 0 
        # solving for quadratic, with a=1, b=1,and c=-2n
        # we get k = int(-1/2+(1+8*n)^0.5/2) 
        
        return int(-1/2+sqrt(1+8*n)/2) 
# @lc code=end

