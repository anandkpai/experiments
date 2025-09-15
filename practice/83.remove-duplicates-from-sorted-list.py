#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

from typing import Optional 
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mark = head 
        while head:
            while head.val == (head.next.val if head.next else None):
                head.next = head.next.next
            head = head.next
        return mark 
        
# @lc code=end

