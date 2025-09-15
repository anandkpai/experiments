#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def createPows(n=10):
        cache = [1]
        for _ in range(n):
            cache.append(cache[-1]*3)
        return set(cache), cache[-1]

    _cache, _max = createPows(20) 

    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False 
        if n in self._cache:
            return True 
        if n < self._max: 
            return False         
        if n%self._max: 
            return False 
        return self.isPowerOfThree(n//self._max)


# @lc code=end

if __name__ == '__main__':
    print(Solution().isPowerOfThree(177147))
