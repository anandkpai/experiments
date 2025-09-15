#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def createPows(n=10):
        cache = [1]
        for _ in range(n):
            cache.append(cache[-1]*4)
        return set(cache), cache[-1]

    _cache, _max = createPows(20) 

    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False 
        if n in self._cache:
            return True 
        if n < self._max: 
            return False         
        if n%self._max: 
            return False 
        return self.isPowerOfFour(n//self._max)

# @lc code=end

