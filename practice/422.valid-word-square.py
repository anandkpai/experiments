#
# @lc app=leetcode id=422 lang=python3
#
# [422] Valid Word Square
#
from typing import List 
# @lc code=start
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        slen = len(words)
        for i in range(slen):
            if len(words[i]) > slen:
                return False 
            for j in range(i+1,slen):
                leftChar = words[i][j] if j < len(words[i]) else ''
                rghtChar = words[j][i] if i < len(words[j]) else ''
                # print(i,j,leftChar,rghtChar)

                if not leftChar == rghtChar:
                    return False 
        return True 
        
# @lc code=end

# print(Solution().validWordSquare(["abc","b"]))