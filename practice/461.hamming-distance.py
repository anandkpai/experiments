#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = format(x,'016b')
        by = format(y,'016b')
        return len([True for x,y in zip(bx,by) if x != y])

# @lc code=end

print(Solution().hammingDistance(1,4))