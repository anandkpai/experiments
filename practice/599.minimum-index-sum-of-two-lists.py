#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#
from typing import List 
# @lc code=start

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        results = []

        if len(list1) > len(list2):
            list1, list2 = list2, list1

        d = {word:idx for  idx,word in enumerate(list1)}

        minSum = float('inf')
        for idx,word in enumerate(list2):
            if idx > minSum:
                break 
            prev_idx = d.get(word)
            if prev_idx is not None:
                newSum = prev_idx + idx
                if minSum > newSum:
                    results = [word]
                    minSum = newSum
                elif minSum == newSum :                    
                    results.append(word)
            
        return results 


        
                
# @lc code=end

