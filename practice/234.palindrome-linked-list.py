#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def vals(self):
    yield self.val
    if self.next:
        yield from self.next.vals()

# monkey patch 
ListNode.vals = vals

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        vals = []
        while head:
            vals.append(head.val)
            head = head.next 
        midp = len(vals) // 2 
        if len(vals)%2 == 0 : 
            return vals[:midp:] == list(reversed(vals[midp::]))
        return vals[:midp:] == list(reversed(vals[midp+1::]))
        
# @lc code=end

