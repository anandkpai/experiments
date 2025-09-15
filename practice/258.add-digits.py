#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num//10 > 0 : 
            num = sum(map(int, str(num)))
        return num 
        
# @lc code=end

