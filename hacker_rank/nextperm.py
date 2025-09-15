from itertools import permutations
from typing import * 
from random import choice, choices

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        inflexion_point = -1
        for i in range(len(nums)-1, 0,-1):
            if nums[i] > nums[i-1]:
                inflexion_point = i-1
                break 
        
        if inflexion_point == -1 :  # the current permutation is the highest possible
            nums.sort()
            return 
        

        rightArray = nums[inflexion_point+1:]
        inflex_val = nums[inflexion_point]
        lowestVal = min(filter(lambda n:n>inflex_val, rightArray))
        nums[inflexion_point] = lowestVal
        rightArray[rightArray.index(lowestVal)] = inflex_val
        rightArray.sort()
        for i in range(len(rightArray)):
            nums[inflexion_point+i+1] = rightArray[i]

        # done




## main ## 

nums  = list(choices(population=range(10), k=choice(range(3,10))))
print(nums)

# brute force
p = sorted(set(permutations(nums)))
n = p.index(tuple(nums))
print(p[n])
print(p[n+1])

Solution().nextPermutation(nums)
print(nums)

