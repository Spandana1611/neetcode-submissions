# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and root.right:
            if root.left.val < root.val and root.right.val > root.val:
                return self.fun(root.left, root.val, -1001, root.val) and self.fun(root.right, root.val, root.val, 1001)
            return False
        if root.left:
            if root.left.val<root.val:
                return self.fun(root.left, root.val, -1001, root.val)
            return False
        if root.right:
            if root.right.val > root.val:
                return self.fun(root.right, root.val, root.val, 1001)
            return False
        return True


    def fun(self, root: Optional[TreeNode], parent: int, mini: int, maxi: int) -> bool:
        if not root:
            return True
        if root.left and root.right:
            if root.left.val <= mini or root.left.val>=maxi or root.right.val <= mini or root.right.val>=maxi:
                return False
            if root.left.val < root.val and root.right.val > root.val:
                return self.fun(root.left, root.val, mini, min(maxi, root.val)) and self.fun(root.right, root.val, max(mini, root.val), maxi)
            return False
        if root.right:
            if root.right.val <= mini or root.right.val>=maxi:
                return False
            if root.right.val > root.val:
                return self.fun(root.right, root.val, max(mini, root.val), maxi)
            return False
        if root.left:
            if root.left.val <= mini or root.left.val>=maxi:
                return False
            if root.left.val < root.val:
                return self.fun(root.left, root.val, mini, min(maxi, root.val))
            return False
        return True
        