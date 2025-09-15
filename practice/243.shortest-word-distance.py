#
# @lc app=leetcode id=243 lang=python3
#
# [243] Shortest Word Distance
#
from typing import List 
# @lc code=start
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDist = len(wordsDict)
        lastWord = ''
        lastIdx = -1 
        for (idx,word) in enumerate(wordsDict):
            if word == word1:
                if lastWord == word2:
                    minDist = min(minDist, idx-lastIdx)
                lastWord = word1 
                lastIdx  = idx    
            elif word == word2:
                if lastWord == word1:
                    minDist = min(minDist, idx-lastIdx)
                lastWord = word2 
                lastIdx  = idx    
        return minDist
        
# @lc code=end

