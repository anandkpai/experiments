#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#
from collections import Counter 
# @lc code=start
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(map(lambda v:v%2, Counter(s).values())) <= 1 
        
# @lc code=end

