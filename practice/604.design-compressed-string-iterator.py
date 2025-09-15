#
# @lc app=leetcode id=604 lang=python3
#
# [604] Design Compressed String Iterator
#
import regex as re
# @lc code=start

class StringIterator:

    def __init__(self, compressedString: str):
        slist = []
        for s in  reversed(re.findall('[a-zA-Z]\d{1,}', compressedString)):
            slist.append(s[0])
            slist.append(int(s[1:]))        
        self.cache = slist         
        

    def next(self) -> str:
        if not self.cache:
            return ' '
        self.cache[-1] -=1
        if self.cache[-1] == 0:
            self.cache.pop()
            return self.cache.pop()            
        else:
            return self.cache[-2]

    def hasNext(self) -> bool:
        return bool(self.cache)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

s = StringIterator("L10e2t1C1o1d1e11")

print(s.next())
print(s.next())
print(s.next())
print(s.next())
print(s.next())
print(s.next())
print(s.hasNext())
print(s.hasNext())