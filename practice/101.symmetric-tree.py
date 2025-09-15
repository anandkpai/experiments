#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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

    def flip(self,p:Optional[TreeNode]):
        p.left, p.right = p.right, p.left 
        if p.left:
            self.flip(p.left)
        if p.right:
            self.flip(p.right)
    

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if no leaves, it is 
        if root.left is None and root.right is None:
            return True
        # now that we have checked for no leaves, if one of the 
        # leaves is missing, it is not
        if root.left is None or root.right is None:
            return False 
        # flip the tree to make a mirror image
        self.flip(root.right)
        # test for mirror image match 
        return self.isSameTree(root.left, root.right)
        
# @lc code=end

