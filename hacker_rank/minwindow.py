from typing import *
from collections import Counter

class Solution:
    def dictAcontainsB(self, a:dict, b:dict)-> bool:
        # compares two dictionaries and decides if a contains b
        if bool(set(b.keys())-set(a.keys())) : # b has keys that a does not        
            return False 

        # for all keys in b, a should have at least the same
        # number of items
        return all(map(lambda k:a[k]>=b[k],b.keys()))



    def minWindow(self, s: str, t: str) -> str:
        # get the t of the substring
        freqChars = dict(Counter(list(t)))
        setChars = set(freqChars.keys())

        # first just check that this is possible
        if not self.dictAcontainsB(Counter(list(s)), freqChars):
            return ''

        minWindowStr = s
        for i in range(len(s)-len(t)+1):
            if s[i] not in setChars : # not a valid start
                continue

            # look for each char    
            k = i
            f = freqChars.copy()
            c = setChars.copy()
            while sum(f.values()) > 0  and k < len(s) and k-i < len(minWindowStr) :
                if s[k] in c:
                    if f[s[k]] == 0 :
                        c.remove(s[k])
                    else: 
                        f[s[k]] -= 1
                k += 1
            
            if sum(f.values()) == 0 : # we found a match 
                if k-i < len(minWindowStr):
                    minWindowStr = s[i:k]
                    # since the answer is unique, worth checking if we done
                    if len(minWindowStr) == len(t):
                        break

        return minWindowStr




if __name__ == "__main__":
    s = "ab"
    t = "b"

    print(Solution().minWindow(s,t))