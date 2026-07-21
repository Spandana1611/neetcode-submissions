# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findGoodNodes(self, root: TreeNode, base: int) -> int:
        if not root:
            return 0
        if root.val >= base:
            return 1 + self.findGoodNodes(root.left, root.val) + self.findGoodNodes(root.right, root.val)
        else:
            return self.findGoodNodes(root.left, base) + self.findGoodNodes(root.right, base)


    def goodNodes(self, root: TreeNode) -> int:
        return self.findGoodNodes(root, root.val)
