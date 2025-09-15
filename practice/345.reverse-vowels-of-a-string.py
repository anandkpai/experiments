#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    _cache = set(['a','e','i','o','u'])
    _cache = _cache.union(map(lambda x:x.upper(), _cache))    
    def reverseVowels(self, s: str) -> str:
        slist = list(s)
        vowlist = [(idx,ch) for idx,ch in enumerate(slist) if ch in self._cache ]
        if not vowlist:
            return s
        locs,chs = zip(*vowlist)
        for idx,ch in zip(locs,reversed(chs)):
            slist[idx] = ch
        return ''.join(slist)
        

        
# @lc code=end

