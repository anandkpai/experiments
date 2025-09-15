from typing import *

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        eligibles = sorted(enumerate(nums), key=lambda t:(t[1],t[0]))
        prevIndex, prevVal  = eligibles[0]
        for (index,val) in eligibles[1:]:
            if val == prevVal :
                if index - prevIndex <= k : return True
        return False 
    

print(Solution().containsNearbyDuplicate([1,0,1,1],1))