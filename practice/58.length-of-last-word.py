#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0        
        found = False

        for c in reversed(s):

            if c != ' ' :
                found = True
                count += 1
                continue 

            if found:
                break 

        return count
        
# @lc code=end

if __name__=='__main__':
    s = "   fly me   to   the moon  "
    print(Solution().lengthOfLastWord(s))
