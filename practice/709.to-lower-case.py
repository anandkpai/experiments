#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
class Solution:
    
    def toLowerCase(self, s: str) -> str:
        return ''.join([c if ord(c)<91 else chr(ord(c)+22) for c in s])
# @lc code=end

