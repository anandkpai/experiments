#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False 
        if set(s) != set(goal):
            return False 
        mismatch_found = 0
        prevs = ''
        prevg = ''
        for ch1,ch2 in zip(s,goal):
            if ch1 != ch2:
                if mismatch_found == 2:
                    return False 
                if prevs and prevg:
                    if prevs != ch2 and prevg != ch1: 
                        return False 
                mismatch_found +=1
                prevs = ch1
                prevg = ch2

        if  mismatch_found == 2:
            return True
        if mismatch_found == 1 : 
            return False 
        if mismatch_found == 0 :
            return  len(s)>len(set(s))


# @lc code=end

