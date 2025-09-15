#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
from primePy import primes



# @lc code=start
class Solution:
    def primes_squares():
        """Generate primes up to n inclusive."""
        n = 65536
        sieve = [True] * (n + 1)
        sieve[0:2] = [False, False]
        for i in range(2, 256 + 1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        return [i*i for i, isprime in enumerate(sieve) if isprime]

    _sqrs = primes_squares()

    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 : 
            return True 
        oNum = num 
        for sqr in self._sqrs:
            if sqr > oNum : 
                return False 
            while not num%sqr:
                num = num//sqr
            if num == 1 : 
                return True

        return False     
        
        
        
# @lc code=end

if __name__ == '__main__':
    isPerfectSquare = Solution().isPerfectSquare
    for i in range(10, 17):
        print(i,isPerfectSquare(i), sep=':', end=' ')