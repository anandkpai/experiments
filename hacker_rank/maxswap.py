from typing import * 

class Solution:
    def maxSwapStr(self, strNums:List[str])->List[str]:
        if len(strNums) == 1 : return strNums
        # find the maxval, start from the end 
        maxValIndex = len(strNums) - strNums[::-1].index(max(strNums)) -1
        if strNums[0] == strNums[maxValIndex]: # no point in swapping, look for the next  
            return strNums[0] + self.maxSwapStr(strNums[1:])
        else : 
            strNums[0], strNums[maxValIndex] = strNums[maxValIndex], strNums[0]
            return strNums




    def maximumSwap(self, num: int) -> int:
        numsStr = list(str(num))
        newNums = self.maxSwapStr(numsStr)
        return int(''.join(newNums))
    

print(Solution().maximumSwap(2736))