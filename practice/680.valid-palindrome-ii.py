#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def checkPalindrome(self, s:str,left:int,right:int):
        while left < right : 
            if s[left] != s[right]:
                return False 
            left +=1 
            right -= 1
        return True 

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left  < right: 
            if s[left] != s[right]:
                if self.checkPalindrome(s,left+1, right):
                    return True 
                elif self.checkPalindrome(s,left, right-1):
                    return True
                else:
                    return False 
            left += 1
            right -= 1
        
        return True 
 

                    
                   
        
# @lc code=end

