#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def isSubstr(self,s:str,offset:int,goal:str):
        for c in goal:
            if offset == len(s):
                break
            if s[offset] != c :
                return False 
            offset += 1
        return True 


    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False 
        if s == goal :
            return True 
        for offset in range(len(s)):
            if self.isSubstr(s,offset,goal):
                if s[:offset:] == goal[-offset::]:
                    return True 
        return False 
        
# @lc code=end

s = "abcde"
goal = "abcde"

print(Solution().rotateString(s,goal))
