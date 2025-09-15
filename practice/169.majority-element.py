#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List 
from collections import defaultdict
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        lim = len(nums)//2
        for n in nums:
            d[n] += 1
            if d[n] > lim :
                return n
            
        # problem states that majority element always exists     
        raise ValueError('no majority element found in {nums}')
        
# @lc code=end

