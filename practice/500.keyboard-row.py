#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#
from typing import List 
# @lc code=start
class Solution:
    _first = set(list("qwertyuiop"))
    _secnd = set(list("asdfghjkl"))
    _third = set(list("zxcvbnm"))
    _cache = [_first,_secnd,_third]

    def findWords(self, words: List[str]) -> List[str]:
        valid = []
        for word in words:
            wset = set(list(word.lower()))
            for row in self._cache:
                if not (wset-row):
                    valid.append(word)
                    break 

        return valid 

        
# @lc code=end

