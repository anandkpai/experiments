#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeropos = deque()
        for idx,val in enumerate(nums):
            if val == 0:
                zeropos.append(idx)
            else:
                if zeropos:
                    pos = zeropos.popleft()
                    nums[pos] = val 
                    nums[idx] = 0 
                    zeropos.append(idx)
                    


        


            
        


# @lc code=end

