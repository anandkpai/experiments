#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#
from typing import List 


# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True 

        intervals.sort()
        prev_end = -1
        for start_t, end_t in intervals:
            if start_t < prev_end :
                return False 
            prev_end = end_t
        return True 




# @lc code=end

