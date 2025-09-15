#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sl = []
        tl = []
        for c in s:
            if c == '#':
                if sl:
                    sl.pop()
            else : 
                sl.append(c)
        for c in t:
            if c == '#':
                if tl:
                    tl.pop()
            else : 
                tl.append(c)

        return sl == tl 

        
# @lc code=end

