#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 : 
            return 0 
        arr = [0,1]
        for _ in range(2,n+1):
            arr.append(arr[-1]+arr[-2])
        return arr[-1]
# @lc code=end

