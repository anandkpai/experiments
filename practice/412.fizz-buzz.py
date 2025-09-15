#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
from typing import List
# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = list(range(1,n+1))
        answer[2::3] = ['Fizz'] * len(answer[2::3])
        answer[4::5] = ['Buzz'] * len(answer[4::5])
        return answer
        
# @lc code=end

