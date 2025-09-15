from typing import *
import heapq 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(self.linkListAsList([]))
    
    def linkListAsList(self,runningList=None):
        if runningList is None:
            runningList = []

        runningList.append(self.val)
        if self.next:
            return self.next.linkListAsList(runningList)
        
        return runningList
    
    
    @staticmethod
    def linkList(l:List):
        zeroNode = ListNode(l[0])
        currentNode = zeroNode

        for node in l[1:]:
            currentNode.next = ListNode(node)
            currentNode = currentNode.next
        
        return zeroNode

        
def monkey_patch_lt(self, other):
    return self.val < other.val 

# monkey patch link list class LinkNode
ListNode.__lt__ = monkey_patch_lt



    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        currentNode = dummy
        nodesHeapList = []

        # populate the heap
        for node in lists:
            heapq.heappush(nodesHeapList, node)

        # read the heap 
        while nodesHeapList:
            lowestNode = heapq.heappop(nodesHeapList)
            currentNode.next = lowestNode
            heapq.heappush(nodesHeapList, lowestNode.next)
            currentNode = currentNode.next

        # return the top of the linklist
        return dummy.next 




if __name__=="__main__":
    rawLists = [[1,4,5],[1,3,4],[2,6]]
    nodesList = [ListNode.linkList(l) for l in rawLists]
    print(nodesList)
    print(Solution().mergeKLists(nodesList))
        
