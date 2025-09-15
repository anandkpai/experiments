from numpy.random import rand
from random import randint
from bisect import bisect_left, bisect_right
from statistics import median

def sortedRandomArray()->list:
    arraySize = randint(4,10)
    return sorted(map(lambda x : int(x*10), rand(arraySize)))


class Solution:
    def sortedMerge(self, nums1: list[int], nums2: list[int], stop_at=None):
        if stop_at is None : 
            stop_at = len(nums1) + len(nums2)
        leftIter = iter(nums1)
        rightIter = iter(nums2)

        leftVal = next(leftIter, None)
        rightVal = next(rightIter, None )
        mergedArray = []

        for _ in range(stop_at):
            if leftVal is None: 
                mergedArray.append(rightVal)
                mergedArray.extend(rightIter)
                break
            elif rightVal is None:
                mergedArray.append(leftVal)
                mergedArray.extend(leftIter)
                break
            else:
                if leftVal > rightVal : 
                    mergedArray.append(rightVal)
                    rightVal = next(rightIter, None)
                else:
                    mergedArray.append(leftVal)
                    leftVal = next(leftIter, None)

        return mergedArray[:stop_at]
        

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        upperMedianIndexNums1 = len(nums1)//2
        upperMedianIndexNums1 -= 1 if len(nums1) % 2 == 0 else 0
        upperMedianIndexNums2 = len(nums2)//2
        upperMedianIndexNums2 -= 1 if len(nums2) % 2 == 0 else 0

        if nums1[upperMedianIndexNums1] > nums2[upperMedianIndexNums2]:
            leftArray = nums2
            leftUIndex = upperMedianIndexNums2
            rightArray = nums1
        else: 
            leftArray = nums1
            leftUIndex = upperMedianIndexNums1
            rightArray = nums2

        lenMergedArray = len(nums1)+len(nums2)
        isEven   =  bool(lenMergedArray %2 == 0)

        # since by construction, the left median val is higher than the right, all values in the leftArray
        # above median can be in the top of a fully merged array 

        # using biSort Search, we find the the point in the right Array where all values are less than the 
        # left Median 
        rightArrayleftPos = bisect_left(rightArray, leftArray[leftUIndex])

        # the left Array Slice will start at the leftUIIndex 
        leftArraySlice = leftArray[leftUIndex:]

        # the median value in the merged array would 
        medianUpperIndex = lenMergedArray//2
        medianUpperIndex -= 1 if  isEven else 0

        # hence in a merged array with all the values above the left Median Upper Index dropped, 
        medianAdjustUpperIndex = medianUpperIndex - leftUIndex - rightArrayleftPos
        
        # the right array slice starts at the point where the left index value would be 
        rightArraySlice = rightArray[rightArrayleftPos:]

        mergedArray = self.sortedMerge(leftArraySlice, rightArraySlice, medianAdjustUpperIndex+2)

        median = (mergedArray[medianAdjustUpperIndex] + mergedArray[medianAdjustUpperIndex+1])/2.0 if isEven else mergedArray[medianAdjustUpperIndex]

        return median


    












    

if __name__=="__main__":
    # nums1 = sortedRandomArray()
    # nums2 = sortedRandomArray()

    nums1 = [1,2]
    nums2 = [3,4]

    print(nums1, nums2, sorted(nums1+nums2), median(nums1+nums2))

    print(Solution().findMedianSortedArrays(nums1,nums2))        

