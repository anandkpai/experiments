from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def findValidPaths(self, root: Optional[TreeNode], targetSum: int, pathsList:List, currentPathList:List):
        if root.val == targetSum : 
            if root.left or root.right: 
                return 
            currentPathList.append(root.val)
            pathsList.append(currentPathList)
            return


        currentPathList.append(root.val)
        targetSum -= root.val 
        if root.left:
            self.findValidPaths(root.left, targetSum, pathsList, currentPathList.copy())
        if root.right:
            self.findValidPaths(root.right, targetSum, pathsList, currentPathList.copy())

        return         



    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root : return []
        if root.val == targetSum : 
            if root.left or root.right: 
                return []
            return [[root.val]]
        pathsList = []
        currentPathList = [root.val]
        targetSum -= root.val 
        if root.left:
            self.findValidPaths(root.left, targetSum, pathsList, currentPathList.copy())
        if root.right:
            self.findValidPaths(root.right, targetSum, pathsList, currentPathList.copy())
        
        return pathsList
    
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(-2)
root.left.left.left = TreeNode(-1)

print(Solution().pathSum(root,-1))