from typing import *
from collections import Counter

class Solution:
    def yield_substrings_chunks(self, s:str, of_size:int):
        # we use a yield function here because we might 
        # not need to go through all the chunks
        for i in range(0,len(s),of_size):
            yield s[i:i+of_size]

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answers=set()
        setWords = set(words)
        freqWords = dict(Counter(words))

        wordLength = len(words[0]) # all the words are the same length
        substringLength = wordLength * len(words)   

        for i in range(len(s)-substringLength+1):
            substring = s[i:i+substringLength]
            possiblyValid = True
            freqSub = dict()
            for chunk in self.yield_substrings_chunks(substring, wordLength):
                # if the chunk is not in the words set, the substring is not valid
                if chunk not in setWords: 
                    possiblyValid = False
                    break 
                freqSub[chunk] = freqSub.get(chunk,0) + 1
            if not possiblyValid:
                continue
            
            if freqSub == freqWords:  # the permutation exists
                answers.add(i)

       
        return list(answers)


if __name__ =='__main__':
    words = ["word","good","best","good"]
    s = "wordgoodgoodgoodbestword"
    
    print(Solution().findSubstring(s,words))