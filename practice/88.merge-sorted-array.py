#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # to do this in place, we have to start from the end 
        end = m+n-1
        m -=1 
        n -=1 
        while end > -1  :
            if m > -1 and n > -1 and nums1[m] >= nums2[n]:
                nums1[m], nums1[end] = nums1[end], nums1[m]
                m -= 1 
            elif n > -1 : 
                nums1[end] = nums2[n]
                n -= 1
            end -= 1
            # print(f'm {m},n {n}, end {end}, nums1 {nums1},nums2 {nums2}')




# @lc code=end

