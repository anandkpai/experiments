#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List 
# @lc code=start

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProf  = 0 
        for price in prices:
            maxProf  = max(price-minPrice, maxProf)
            minPrice = min(price, minPrice)

        return maxProf

# @lc code=end

