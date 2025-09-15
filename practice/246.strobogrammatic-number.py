#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#

# @lc code=start
class Solution:
    _cmap = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
    def isStrobogrammatic(self, num: str) -> bool:
        slist = []
        for c in reversed(num):
            if c not in self._cmap:
                return False 
            slist.append(self._cmap[c])
        return ''.join(slist) == num

# @lc code=end

