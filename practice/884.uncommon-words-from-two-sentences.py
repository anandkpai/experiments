#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        set1 = set(s for s,f in Counter(s1).items() if f == 1)
        set2 = set(s for s,f in Counter(s1).items() if f == 1)
        return List((set1-set2).union(set2-set1))
        
        
        
# @lc code=end

