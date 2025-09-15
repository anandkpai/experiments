class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 : 
            if n == 0 : 
                raise ValueError('invalid input')
            else : 
                return 0 
        if n == 0 :
            return 1

        return self.recPow(x,n)

    def recPow(self, x:float, n:int) -> float:
        if n == 1 : return x
        if n == 0 : return 1 
        leftPow = n // 2
        rightPow = n - leftPow 

        leftPowVal  = self.recPow(x,leftPow)
        leftPowSq = leftPowVal*leftPowVal 
        if leftPow == rightPow:
            return leftPowSq
        else :
            return leftPowSq *x
        
print(Solution().myPow(2,10))