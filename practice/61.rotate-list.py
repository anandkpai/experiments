#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
from collections import deque

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        keep = head 
        cache = deque()
        endNode = None
        while head:
            cache.append(head)
            head = head.next
            if len(cache) > k:
                endNode = cache.popleft()
        

        if endNode is not None:
        # the top of the cache is the last one, 
        # the next after that is the new head 
        # the bottom is where the old head gets added back 
            
            endNode.next = None
            cache[-1].next = keep
            return cache[0]

        # otherwise, it means that k > length of the list. The cache 
        # has the whole list 
        k = k%len(cache)
        cache[-k-1].next = None
        cache[-1].next = cache[-k]
        return cache[-k]

        
# @lc code=end

if __name__ == '__main__':
    marker = ListNode()
    node = marker
    for val in range(1,6):
        node.next = ListNode(val)
        node = node.next 
    head = marker.next 
    s = Solution()
    head = s.rotateRight(head,2)
    print('returned')
    while head:
        print(head.val)
        head = head.next



