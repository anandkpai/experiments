from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s : return 0
        if len(s) == 1 : return 1
        maxlen = 0
        i = 0
        currentSet = set()
        while i < len(s)-maxlen:
            currentSet.add(s[i])
            founddup = False
            for j in range(i+len(currentSet),len(s)):
                if s[j] in currentSet:
                    maxlen = max(maxlen,len(currentSet))
                    currentSet.remove(s[i])
                    i += 1
                    founddup = True
                    break
                else : 
                    currentSet.add(s[j])
            if not founddup : 
                maxlen = max(maxlen, len(currentSet))
                break

        return maxlen
        

print(Solution().lengthOfLongestSubstring('anviaj'))