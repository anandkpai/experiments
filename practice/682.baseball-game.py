#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#
from typing import List
# @lc code=start
class Solution:
    
    def calPoints(self, operations: List[str]) -> int:
        cache = []
        for op in operations:
            if op.isdigit() or op[0]=='-':
                cache.append(int(op):)
            elif op == '+':
                cache.append(cache[-1]+cache[-2])
            elif op == 'D':
                cache.append(2*cache[-1])
            elif op == 'C':
                cache.pop()
            else:
                raise ValueError(f'invalid Operation {op}')
            
        return sum(cache)
# @lc code=end
ops = ["5","-2","4","C","D","9","+","+"]

print(Solution().calPoints(ops))
