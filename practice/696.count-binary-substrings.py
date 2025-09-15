#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#
import regex as re
# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        idx = 0
        tcount = 0 
        lens = len(s)
        while idx < lens:
            s1count=1
            schar = s[idx]
            while idx+s1count < lens and s[idx+s1count] == schar:
                s1count +=1 
            idx += s1count 
            if idx == lens:
                break 
            schar = s[idx]
            s2count = 1
            while idx+s2count < lens and s2count < s1count and s[idx+s2count] == schar :
                s2count +=1
            tcount += s2count
        return tcount 



# @lc code=end
s = "00100"
print(Solution().countBinarySubstrings(s))
