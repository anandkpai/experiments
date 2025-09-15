#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
from collections import Counter
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts  = Counter(s).values()                        
        return min(sum(map(lambda x:x-1 if x%2 else x, counts))+1, len(s))
        
        
# @lc code=end

