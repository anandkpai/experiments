#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
from typing import List 
# @lc code=start
from itertools import groupby
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        typg = groupby(typed)
        namg = groupby(name)

        while True:
            tch, tgrp = next(typg,(None,None))
            nch, ngrp = next(namg,(None,None))
            if tch != nch : 
                return False 
            if not tch : # we have already checked that they are the same
                return True 
            if len(list(ngrp)) > len(list(tgrp)):
                return False 
            

        
# @lc code=end

name = "leelee"
typed = "lleeelee"
print(Solution().isLongPressedName(name, typed))