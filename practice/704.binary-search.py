#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
from typing import List
# @lc code=start
from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums,target)
        if idx == len(nums):
            return -1
        return idx if nums[idx] == target else -1

# @lc code=end

