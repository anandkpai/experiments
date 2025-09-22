#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
from typing import List 
# @lc code=start
from collections import Counter
class Solution:
    def common_dict(self,d1:dict, d2:dict)->dict:
        d = dict()
        for k in d1:
            if k in d2:
                d[k] = min(d1[k],d2[k])
        return d


    def commonChars(self, words: List[str]) -> List[str]:
        commonDict = Counter(words[0])
        for word in words:
            commonDict = self.common_dict(commonDict, Counter(word))
        ans = []
        for c in commonDict:
            ans.extend(commonDict[c]*[c])
        return ans 

# @lc code=end

