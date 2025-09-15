#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# import regex as re
from typing import List 
from itertools import groupby
# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = [len(list(g)) for k,g in groupby(nums) if k == 1]
        return max(ones) if ones else 0 

        


            
        
# @lc code=end

print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))