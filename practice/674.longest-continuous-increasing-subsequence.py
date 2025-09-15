#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        mlen = clen = 1 
        for idx in range(1, len(nums)):
            if nums[idx]> nums[idx-1]:
                clen +=1
            else:
                if clen > mlen:
                    mlen = clen
                clen = 1
        return mlen  if mlen > clen else clen 

# @lc code=end

