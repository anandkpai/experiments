from itertools import groupby 
class Solution:
    def countAndSay(self, n: int) -> str:
        cs = []
        for g in groupby(str(n)):
            cs.append(f"{str(len(g))}{g[0]}")
        return ''.join(cs)
    

print(Solution().countAndSay(1))