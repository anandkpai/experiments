#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
from typing import List 
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = -1 
        scost = 0 
        while i < len(cost)-2:
            i+= 1 if cost[i+1] <= cost[i+2]/2 else 2
            scost += cost[i]    
        return scost 
# @lc code=end

cost = [1,100,1,1,1,100,1,1,100,1]
cost = [10,15,20]

print(Solution().minCostClimbingStairs(cost))