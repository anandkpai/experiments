class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        nleft = n//2 
        nright = n - nleft 

        nleft_val = self.myPow(x,nleft)  
        nleft_val_sq = nleft_val * nleft_val 
        if nleft == nright:
            return nleft_val_sq
        else :
            return nleft_val_sq * x
        


print(Solution().myPow(2.4,10))