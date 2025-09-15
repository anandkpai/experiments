#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
from collections import Counter
from math import gcd
from functools import reduce 


# @lc code=start
class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
    
# @lc code=end

s = "ababab"
print(Solution().repeatedSubstringPattern(s))