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

        






class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self,other):
        return self.node.val < other.node.val 
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        zeroNode = ListNode(0)
        currentNode = zeroNode
        nodeHeap =[]

        
        for listNode in lists:
            if listNode : 
                heapq.heappush(nodeHeap, HeapNode(listNode))

        while nodeHeap:
            heap_node = heapq.heappop(nodeHeap)
            node = heap_node.node
            currentNode.next = node
            currentNode = currentNode.next
            if currentNode.next :
                heapq.heappush(nodeHeap,HeapNode(currentNode.next))

        return zeroNode.next



if __name__=="__main__":
    rawLists = [[1,4,5],[1,3,4],[2,6]]
    nodesList = [ListNode.linkList(l) for l in rawLists]
    print(nodesList)
    print(Solution().mergeKLists(nodesList))
        
