#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#
from typing import List 
# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes5 = 0
        notes10 = 0
        for bill in bills:
            if bill == 5:
                notes5 +=1 
                continue
            if notes5 == 0:
                return False
            if bill == 10:
                notes5  -= 1
                notes10 += 1
            if bill == 20:
                if notes10 == 0 and notes5 < 3:
                    return False 
                if notes10>0:
                    notes10 -= 1
                    notes5  -= 1
                else :
                    notes5  -=3
        return True             



        
# @lc code=end

bills = [5,5,10,10,20]
print(Solution().lemonadeChange(bills ))