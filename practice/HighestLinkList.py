from typing import Deque, Optional 

class HighestLinkList():
    def __init__(self,vals:Deque[int]):
        if not isinstance(vals, Deque):
            vals = Deque(vals)
        self.val: Optional[int] = None
        self.next  = None
        if vals:
            self.val = vals.popleft()
            self.next = HighestLinkList(vals)
        
        def add(self,val):
            if val < self.val :
                if self.next:
                   self.next.add(val) 
                else:
                    self.next = HighestLinkList([vals])    

    # helper to collect values (non-recursive; safe for long lists)
    def _collect_vals(self):
        vals = []
        cur = self
        # (optional) cycle guard: track visited nodes or limit length
        while cur is not None and cur.val is not None:
            vals.append(cur.val)
            cur = cur.next
        return vals

    def __str__(self):
        # human-friendly
        return ",".join(map(str, self._collect_vals()))

    def __repr__(self):
        # developer-friendly
        return f"Node({self._collect_vals()!r})"

h = HighestLinkList([4,3,1])
print(h)
