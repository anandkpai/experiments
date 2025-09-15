#
# @lc app=leetcode id=598 lang=python3
#
# [598] Range Addition II
#
from typing import List
# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # the max value is simply the count of the # of entries in ops.
        # the number of cells that get that max value is the 
        # rectangle of the minimum of the values for each a,b in the operation
        if ops:
            xlist, ylist = zip(*ops)
            return min(xlist)*min(ylist)
        else:
            return m*n 

# @lc code=end

m = 3
n = 3 
ops = [[2,2],[3,3]]

print(Solution().maxCount(m,n,ops))