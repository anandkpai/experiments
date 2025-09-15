from typing import *
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val 

    def __iter__(self):
        current = self
        while current:
            yield current.val
            current = current.next 

        
    
    def nodesAsList(self, prevList=None):
        if not prevList: 
            prevList = []
        prevList.append(self)
        if self.next:
            self.next.nodesAsList(prevList)
        
        return prevList
    
    def __repr__(self):        
        return ':'.join(map(lambda n:str(n.val), self.nodesAsList()))


def nodeFromList(l:List[int]):
    l = list(l)
    current = node = ListNode(l[0])
    for val in l[1:]:
        current.next = ListNode(val)
        current = current.next

    return node

l = [[1,4,5,6,7,8,9],[1,3,4],[2,6]]

nodes = []
for nlist in l:     
    nodes.append(nodeFromList(nlist))

print(list(heapq.merge(*list(map(iter,nodes)))))







