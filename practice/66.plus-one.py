#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0 
        addval = 1
        for idx in range(len(digits)-1, -1,-1):
            newVal = digits[idx] + addval + carry 
            addval = 0 
            if newVal > 9:
                carry = 1
                newVal -= 10 
            else : 
                carry = 0 

            digits[idx] = newVal
            if not carry : 
                break 

        if carry:
            digits.insert(0,1)

        return digits


# @lc code=end

