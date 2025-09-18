#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#
from typing import List
# @lc code=start
from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freqs = set(Counter(deck).values())
        g = gcd(*freqs)
        return g > 1  

# @lc code=end

