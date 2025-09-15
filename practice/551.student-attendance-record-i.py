#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1 : 
            return False 
        for s_sub in s.split('A'):
            if len(max(s_sub.split('P'), key=len)) > 2:
                return False
        return  True 
        
# @lc code=end

