#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#
from typing import List
# @lc code=start
class Solution:

    def test(self, num):
        for ch in str(num):
            d = ord(ch)-48
            if d == 0 or num%d:
                return False
        return True 

    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [num for num in range(left,right+1) if self.test(num)]


        
# @lc code=end

