#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        dupchars = set()
        for idx,c in enumerate(list(s)):
            if c in dupchars:
                continue
            if c in d:
                d.pop(c)
                dupchars.add(c)
            else :
                d[c]=idx
        
        return next(iter(d.values()),-1)



# @lc code=end

print(Solution().firstUniqChar('leetcode'))