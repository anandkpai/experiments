from collections import Counter
from typing import *

class Solution:
    def twoSumValues(self, nums, target)->List[int]:
        freqCount = Counter(nums)
        # set of all nums 
        numSet = set(freqCount.keys())
        # set of all num elements that have duplicates
        numSetDups = set(map(lambda tup:tup[0],filter(lambda item:item[1]>1, freqCount.items())))
        return self.twoSumWithSets(target, numSet, numSetDups)
    
    def twoSumWithSets(self, target: int, numSet: set, numSetDups:set ) -> List[int]:
        # check for every element. 
        pairsSet = set()
        for num in numSet:
            needed_num = target - num   # since they have to sum up to target
            if needed_num == num: # we are looking for the same value as ourselves
                if num in numSetDups:
                    pairsSet.add((num,num))
            else:
                if needed_num in numSet:
                    pairsSet.add(tuple(sorted([num, needed_num])))
                
        return pairsSet

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # this is an extension of the twosum problem. 
        freqCount = Counter(nums)
        # set of all nums 
        numSet = set(freqCount.keys())
        # set of all num elements that have duplicates
        numSetDups = set(map(lambda tup:tup[0],filter(lambda item:item[1]>1, freqCount.items())))
        # set of all num elements that have triplicates
        numSetTrips = set(map(lambda tup:tup[0],filter(lambda item:item[1]>2, freqCount.items())))

        # now iterate through the values, only need to go till the third last

        triplets = set()
        for val in nums[:-2]: 
            target = -val
            # we have to change the sets we send, since we are making one of the elements a target
            if val in numSetTrips: # change nothing
                pairs = self.twoSumWithSets(target, numSet, numSetDups)
            elif val in numSetDups: # it is not in triplicate, so we must remove it from duplicates
                pairs = self.twoSumWithSets(target, numSet, numSetDups -set([val]))
            else : # it is not in duplicates, remove it completely
                pairs = self.twoSumWithSets(target, numSet - set([val]), numSetDups)

            for pair in pairs:
                l = list(pair)
                l.append(val)
                triplets.add(tuple(sorted(l)))

        return list(triplets)

        
    


if __name__=='__main__':
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    s = Solution().threeSum(nums)
    print(s)

    nums = [-1,0,1,2,-1,-2,-3,3,0,4]
    print(Solution().twoSumValues(nums, 4))