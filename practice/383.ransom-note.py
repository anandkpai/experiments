#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
from collections import Counter # @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if set(list(ransomNote))-set(list(magazine)):
            return False 
        r = Counter(ransomNote)
        for c in magazine:
            if c in r:
                if r[c] == 1:
                    r.pop(c)
                else:
                    r[c] -=1
            if not r:
                return True 
            
        return False
    
# @lc code=end

