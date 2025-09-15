from typing import * 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1 : return nums[0]
        s = max(nums)
        if s <= 0 : return s 
        cSum = 0
        cArr = []
        # move the pointer forward till we find the first non negative number
        startPoint = 0 
        while nums[startPoint] <= 0 :
            startPoint += 1
        # also find the end point (will be excluded)
        endPoint = len(nums)        
        while nums[endPoint-1] <= 0 : 
            endPoint -= 1

        for val in nums[startPoint:endPoint]:
            cSum+=val
            cArr.append(cSum)

        (minCArrIndex, minCArrVal) = min(enumerate(cArr), key=lambda t:t[1])
        # have the find the last max value
        (mP, maxCArrVal) = max(enumerate(cArr[::-1]), key=lambda t:t[1])
        maxCArrIndex = len(cArr)- mP - 1 

        print(cArr)

        if maxCArrIndex <= minCArrIndex : return maxCArrVal

        return maxCArrVal - min(minCArrVal,0)
        
    

nums = [3,-2,-3,-3,1,3,0]
print(Solution().maxSubArray(nums))



