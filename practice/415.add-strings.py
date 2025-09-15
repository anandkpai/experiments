#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        nlist1 = list(map(int,str(num1)))
        nlist2 = list(map(int,str(num2)))

        ansC = []
        while nlist1 or nlist2:
                v1 = nlist1.pop() if nlist1 else 0
                v2 = nlist2.pop() if nlist2 else 0
                s12 = v1+v2+carry 
                carry = 1 if s12 > 9 else 0
                ansC.append(s12 if s12 < 10 else s12-10)
        
        return ''.join(map(str,ansC))


# @lc code=end

