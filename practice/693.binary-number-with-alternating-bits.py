#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        brep = list(format(n,'b'))
        for idx in range(1,len(brep)):
            if brep[idx] == brep[idx-1]:
                return False
        return True


# @lc code=end
s = Solution()
for i in [5,7,11]:
    print(s.hasAlternatingBits(i))
