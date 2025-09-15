#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def buildCache():
        powers  = [1]
        for  _ in range(32):
            powers.append(powers[-1]*2)
        return set(powers)

    _cache = buildCache()
    
    def isPowerOfTwo(self, n: int) -> bool:        
        return n in Solution._cache
    
# @lc code=end

