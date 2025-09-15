#
# @lc app=leetcode id=734 lang=python3
#
# [734] Sentence Similarity
#
from typing import List 
# @lc code=start
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False 
        simSet = set(map(tuple, similarPairs))        
        for w1,w2 in zip(sentence1,sentence2):
            if (w1,w2) not in simSet and (w2,w1) not in simSet:
                return False 
        return True 


# @lc code=end

sentence1 = ["great","acting","skills"]
sentence2 = ["fine","drama","talent"]
similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]

print(Solution().areSentencesSimilar(sentence1, sentence2,similarPairs))