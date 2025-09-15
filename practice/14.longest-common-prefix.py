#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List 


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # pick any word to start from
        d = dict(enumerate(list(strs[-1])))

        for word in strs:
            nomatch = -1

            for i in d.keys():
                if i == len(word) or d[i] != word[i]:
                    nomatch = i
                    break 

            if nomatch == 0 : # failed at first letter
                return ''

            # drop all items where there was no match             
            if nomatch > 0  :
                d = dict(list(d.items())[:nomatch:])                


        
        return ''.join(d.values())

        

        

        
# @lc code=end

