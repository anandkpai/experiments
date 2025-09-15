from typing import * 

class Solution:
    def addValidSets(self, availableNumsLeft2Add:set, numsAddedSoFar:set, target:int, krem:int, validSets:set):

        if krem == 1 : 
            if target in availableNumsLeft2Add:
                numsAddedSoFar.add(target)
                validSets.add(tuple(sorted(numsAddedSoFar)))  
            return 

        for num in sorted(availableNumsLeft2Add):
            if num > target : 
                break
            else : 
                newA = availableNumsLeft2Add.copy()
                newA.remove(num)
                newN  = numsAddedSoFar.copy()
                newN.add(num)
                newTarget = target - num 
                nkrem = krem -1 
                self.addValidSets(newA, newN, newTarget, nkrem, validSets)

        if target in availableNumsLeft2Add:
            numsAddedSoFar.add(target)
            validSets.add(tuple(sorted(numsAddedSoFar)))  

        return

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        availableNumsLeft2Add = set(list(range(1,10)))
        numsAddedSoFar = set()
        target = n 
        krem = k 
        validSets = set()
        self.addValidSets(availableNumsLeft2Add,numsAddedSoFar, target, krem, validSets)
        return validSets 
    
print(Solution().combinationSum3(3,7))