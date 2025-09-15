#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#
import regex as re
# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        seqlist = re.findall('[a-z]+|\d+', abbr)
        idx = 0 
        for seq in seqlist:
            if idx >= len(word):
                return False 
            if seq.isdigit():
                if seq[0]=='0':
                    return False
                idx += int(seq)
                continue    
            if seq != word[idx:idx+len(seq):]:
                return False 
            idx += len(seq)
        return idx == len(word) 

        
# @lc code=end

print(Solution().validWordAbbreviation("internationalization","i12iz4n"))