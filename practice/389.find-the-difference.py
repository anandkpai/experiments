#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
from collections import Counter 
# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return (set(Counter(t).items())-(set(Counter(s).items()))).pop()[0]

        
# @lc code=end

