#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# monkey patch equivalent 

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are none, they match 
        if (p is None) and (q is None) :
            return True 
        # since we have passed both being none, now if either is none
        # there is no match 
        if (p is None) or (q is None) :
            return False
        # now check if the val is okay
        if p.val != q.val : 
            return False
        # now recurse for the leaves
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    

        



# @lc code=end

