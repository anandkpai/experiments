#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (not t) :
            return False if s else True 

        
        idx_t = 0 
        for cs in s:
            if idx_t == len(t):
                return False
            while t[idx_t] != cs: 
                if idx_t ==  len(t)-1:
                    return False 
                idx_t +=1                
            idx_t +=1
        return True

        
# @lc code=end

