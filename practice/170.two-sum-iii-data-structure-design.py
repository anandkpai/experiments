#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#

# @lc code=start
class TwoSum:

    def __init__(self):
        self.numbers = set()
        self.dupes = set()

    def add(self, number: int) -> None:
        if number in self.numbers:
            self.dupes.add(number)
        self.numbers.add(number)


    def find(self, value: int) -> bool:

        if value%2 == 0 :
            if  value//2 in self.dupes : 
                return True


        for x in self.numbers:
            if (value-x) in self.numbers and value-x !=x:
                return True
            
        return False 



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end

