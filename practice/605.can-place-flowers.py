#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
from typing import List

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:  
        if n == 0 : return True       
        # little trick, add 0 at the end to make it easier         
        # this also means that when idx = 0, we pick up the 0 we added at the end
        flowerbed.append(0)
        for idx in range(len(flowerbed)-1):
            if  not flowerbed[idx-1] and not flowerbed[idx] and not flowerbed[idx+1]:
                flowerbed[idx] = 1
                n -= 1
                if n == 0 : return True 
        return False 
        
# @lc code=end

