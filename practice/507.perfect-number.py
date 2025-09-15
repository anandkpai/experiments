#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False 
        divisors = [1]
        for i in range(2,int(sqrt(num)+1)):
            if not num%i:
                divisors.append(i)
                divisors.append(num//i)
        
        return sum(divisors) == num
# @lc code=end

