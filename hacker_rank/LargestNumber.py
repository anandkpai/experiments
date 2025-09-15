from typing import *

class Solution:
    class StrClass():
        def __init__(self, s: str):
            self.s = s

        def __lt__(self, other)->bool:
            slist = list(self.s)[::-1]
            olist = list(other.s)[::-1]

            while slist or olist: 
                if slist: 
                    sc = slist.pop()
                if olist:
                    oc = olist.pop()
                if sc != oc : 
                    return bool(sc < oc) 
                
            return False 
                
    def largestNumber(self, nums: List[int]) -> str:
        return ''.join(sorted(map(str, nums), key=  Solution.StrClass , reverse=True)) 
    

print(Solution().largestNumber([34323,3432]))