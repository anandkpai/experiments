from typing import * 



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def as_list(self, l = None):
        if not l:
            l = []
        l.append(self.val)
        if self.next:
            return self.next.as_list(l)
        else:
            return l
        
        def __repr__(self):
            return str(self.as_list())


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0 : 
            return head

        
        current = head
        
        # move till the nth
        for _ in range(n):
            if not current:
                return None
            current = current.next 

        drop_candidate = head 
        drop_candidate_parent = None

        # now keep updating 
        while current:
            current = current.next
            drop_candidate_parent = drop_candidate
            drop_candidate = drop_candidate.next

            

        # now we have the parent of the drop_candidate and it's parent 
        if not drop_candidate_parent :  # the drop candidate is at the top of the list            
            return drop_candidate.next 
        else: 
            drop_candidate_parent.next = drop_candidate.next 
            return head 




    
l = [1,2]    
n = 2
head = ListNode(l[0])
current = head 
for i in range(1,len(l)):
    current.next = ListNode(l[i])
    current = current.next

print(head.as_list())

node = Solution().removeNthFromEnd(head,n) 
if node : 
    print(node.as_list())
else :
    print([])
