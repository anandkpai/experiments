#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#
from typing import List 
from collections import Counter 
# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count =  g_point =   0
        glen = len(g)
        for cookie_size in s :            
            if g[g_point] <= cookie_size:
                count +=1 
                g_point += 1
                if g_point == glen:
                    return count 
        
        return count 

                        

        
# @lc code=end

