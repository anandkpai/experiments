#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

pick = 6
def guess(num: int) -> int:
     if num == pick : return 0 
     if num < pick : return 1
     return -1 

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0




class Solution:
    def guessNumber(self, n: int) -> int:
        top = n
        bot = 1 
        
        while top>bot+1: 

            if  not (g := guess(mid:=(top+bot)//2)) :
                    return mid
            elif g == 1 : 
                bot = mid 
            else : 
                top = mid
        
        return top if not guess(top) else bot 
                 
                
            
        
# @lc code=end

if __name__ == '__main__':
     for pick in range(1,20):
        print(pick, Solution().guessNumber(40))