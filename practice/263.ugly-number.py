#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

from math import sqrt
# @lc code=start
class Solution:
    _cache = [5,3,2]

    def isUgly(self, n: int) -> bool:
        if n == 0 : 
            return False 
        if n == 1 : 
            return True 
        if n < 0 : 
            return False
         
        for d in self._cache:
            while n%d == 0:
                n = n//d

        print(n)
        return not n>6
        
    
        



# @lc code=end

if __name__ == '__main__':
    n = 905391974
    print(Solution().isUgly(n))