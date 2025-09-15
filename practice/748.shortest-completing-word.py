#
# @lc app=leetcode id=748 lang=python3
#
# [748] Shortest Completing Word
#
from typing import List
# @lc code=start
from collections import Counter
from heapq import heapify, heappop
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words_with_len = [(len(word),idx, word) for idx, word in enumerate(words)]
        heapify(words_with_len)
        while words_with_len:
            _,_,word = heappop(words_with_len)
            dword = Counter(word)
            complete = True
            for c in licensePlate.lower():
                if c.isdigit() or c == ' ':
                    continue
                if not c in dword or dword[c] == 0:
                    complete = False
                    break
                dword[c] -= 1
            if complete:
                return word
        
# @lc code=end

licensePlate = "1s3 456"
words = ["looks","pest","stew","show"]

print(Solution().shortestCompletingWord(licensePlate, words))