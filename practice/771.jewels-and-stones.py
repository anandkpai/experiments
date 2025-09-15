#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sj = set(jewels)
        return len([1 for s in stones if s in sj])
        
# @lc code=end

