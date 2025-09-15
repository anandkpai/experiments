from typing import *

class Solution:
    def isValid(self, v:tuple[int,int,int]):
        (x,y,z) = v
        return (x>y>z) or (x<y<z)

    def numTeams(self, rating: List[int]) -> int:
        validCount = 0
        for i in range(len(rating)-2):
            for j in range(i+1,len(rating)-1):
                for k in range(j+1, len(rating)):
                    if self.isValid((rating[i],rating[j], rating[k])):
                        validCount +=1 
        
        return validCount
                    

ratings = [2,5,3,4,1]

print(Solution().numTeams(ratings))