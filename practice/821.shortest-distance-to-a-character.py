#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#
from typing import List 
# @lc code=start
from bisect import bisect_left
from sortedcontainers import SortedSet
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        cpos = []
        cposIdx = -1
        spos = []

        for idx,ch in enumerate(s):
            if ch == c:
                cpos.append(idx)
                cposIdx +=1 
                spos.append((idx,cposIdx,cposIdx))
            else : 
                spos.append((idx,cposIdx,cposIdx+1))
        answer = []
        for idx, left, right in spos:
            if left == right : 
                answer.append(0)
                continue
            leftDiff = idx-cpos[left] if left > -1 else float('inf')
            rightDiff = cpos[right]-idx if right < len(cpos) else float('inf')
            answer.append(min(leftDiff,rightDiff))
        return answer

# @lc code=end

s = "aaab"
c = "b"

print(Solution().shortestToChar(s,c))

