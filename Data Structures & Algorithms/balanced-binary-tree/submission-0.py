# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0, True
        leftHeight, isValid = self.height(root.left)
        if not isValid:
            return None, False
        rightHeight, isValid = self.height(root.right)
        if not isValid:
            return None, False
        if abs(rightHeight - leftHeight) > 1:
            return None, False
        return 1+max(rightHeight, leftHeight), True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h, isvalid = self.height(root)
        return isvalid