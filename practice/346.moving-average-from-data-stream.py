#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#
from collections import deque
# @lc code=start
class MovingAverage:

    def __init__(self, size: int):
        self.stack = deque()
        self.size = size
        self.mavg = 0 

    def next(self, val: int) -> float:
        if (len_s:=len(self.stack)) < self.size:
            self.stack.append(val)
            self.mavg = (self.mavg*len_s+val)/(len_s+1)
        else:            
            self.stack.append(val)
            self.mavg += (val-self.stack.popleft())/self.size 
        return self.mavg




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end

