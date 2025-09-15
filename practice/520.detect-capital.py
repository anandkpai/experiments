#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if  word == word.upper() or word == word.lower() :
            return True
        if word[0] == word[0].upper() and word[1::] == word[1::].lower():
            return True 
        return False 
# @lc code=end

