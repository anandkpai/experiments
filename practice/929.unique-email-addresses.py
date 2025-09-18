#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#
from typing import List 
# @lc code=start
class Email():
    def __init__(self,s:str):
        self.s = s
    
    def _hash_helper(self):
        name, domain = self.s.split('@')
        name = name.replace('.','')
        name = name.split('+')[0]
        return f"{name}@{domain}"

    def  __hash__(self):        
        return hash(self._hash_helper())
        

    def __eq__(self, other):
        if not isinstance(other, Email):
            return False 
        return self.__hash__() == other.__hash__()
    
    def __str__(self):
        return self._hash_helper()
    
    def __repr__(self):
        return self._hash_helper()



class Solution:
    def _hash_helper(self,s:str):
        name, domain = s.split('@')
        name = name.replace('.','')
        name = name.split('+')[0]
        return f"{name}@{domain}"

    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set(map(self._hash_helper,emails )))
    
# @lc code=end

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(emails))