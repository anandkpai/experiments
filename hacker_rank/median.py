from typing import *
from bisect import bisect_left

class Solution:
    def mergeArrays(self, nums1: List[int], nums2: List[int], stop:int)->List[int]:
        num1index = num2index = mergedIndex = 0 
        mergedArray = []
        while num1index < len(nums1) and num2index < len(nums2) and mergedIndex <= stop : 
            mergedIndex += 1
            if nums1[num1index] < nums2[num2index]: 
                mergedArray.append(nums1[num1index])
                num1index += 1
            else :
                mergedArray.append(nums2[num2index])
                num2index += 1
        
        if mergedIndex > stop : return mergedArray
        if num1index == len(nums1) : 
            mergedArray.extend(nums2[num2index:])
        else : 
            mergedArray.extend(nums1[num1index:])

        return mergedArray[:stop+1]

    def getLowerIndexOfMedianForSortedArray(self,nums: List[int])->int:
        upperMedianIndexMergedArray = len(nums)//2
        return upperMedianIndexMergedArray -1 if len(nums) % 2 == 0  else upperMedianIndexMergedArray



    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sizeOfMergedArray = len(nums1)+len(nums2)
        upperMedianIndexMergedArray = sizeOfMergedArray//2

        nums1LowerIndex = self.getLowerIndexOfMedianForSortedArray(nums1)
        nums2LowerIndex = self.getLowerIndexOfMedianForSortedArray(nums2)

        # one of these lower median index values is lower than the other, let's call that the left. 
        if nums1[nums1LowerIndex] < nums2[nums2LowerIndex]:
            leftArray = nums1
            leftLndx  = nums1LowerIndex
            rghtArray = nums2

        else : 
            leftArray = nums2
            leftLndx  = nums2LowerIndex
            rghtArray = nums1

         # when we merge the arrays, for the leftArray, we  can start from the LeftLndx, because everything 
         # above that is above the median of the merged Array

         # similarly for the rightArray, we can also drop everything above the leftArrays leftIndex value, 
         # which we can find efficiently using bisearch   

        rightArrayLeftPos = bisect_left(rghtArray, leftArray[leftLndx])
        mergedArray = self.mergeArrays(leftArray[leftLndx:],rghtArray[rightArrayLeftPos:],upperMedianIndexMergedArray-leftLndx-rightArrayLeftPos)

        if sizeOfMergedArray %2 == 0 : 
            return (mergedArray[-1]+mergedArray[-2])*1.0/2.0
        else :
            return mergedArray[-1]


nums1 = [1,3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))