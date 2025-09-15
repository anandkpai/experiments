from typing import * 

class Solution:
    def findValidSum(self,prevSet:set, setNums:set,validSets:set, target:int, krem:int)->set:
        if krem == 1 :
            if target in setNums:
               prevSet.add(target)
               validSets.add(frozenset(prevSet))     
            return validSets

        

        for val in setNums:
            if val >= target : 
                continue
            rSetNums = setNums.copy()
            rSetNums.remove(val)
            rtarget = target - val 
            rkrem = krem - 1
            rprevSet = prevSet.copy()
            rprevSet.add(val)
            self.findValidSum(rprevSet, rSetNums, validSets, rtarget, rkrem)
            
        return validSets
                            

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # first do a simple check. The absolute minimum sum that can be built 
        # with k numbers is k * (k+1) / 2 , so check that n is larger than that 
        if (k * (k+1))//2 > n : return []
        validSums = set()        
        maxNum = min(9,n)
        for i in range(1,9-k):
            if i > n : 
                break             
            setNums = set(range(1,maxNum+1))
            setNums.remove(i)
            prevSet = set([i])
            target = n - i 
            krem = k-1
            self.findValidSum(prevSet, setNums, validSums, target, krem)            
        
        return validSums



print(Solution().combinationSum3(3,9))