#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#
from typing import List
import regex as re
# @lc code=start
from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banset = set(banned)
        d = defaultdict(int)
        maxCount = (0,0) 
        for word in re.findall('[a-z]{1,}',paragraph.lower()):
            if word in banset : 
                continue
            d[word] += 1
            if d[word] > maxCount[0]:
                maxCount = (d[word], word)

        return maxCount[1]
        
        
# @lc code=end

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(Solution().mostCommonWord(paragraph, banned))