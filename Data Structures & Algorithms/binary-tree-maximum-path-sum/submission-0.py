# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = root.val
        
        def dfs(node: Optional[TreeNode]) -> int: 
            nonlocal maxi
            if not node:
                return 0
            leftSum = 0
            if node.left:
                leftSum += dfs(node.left)
            rightSum = 0
            if node.right:
                rightSum += dfs(node.right)
            
            maxi = max(maxi, node.val, node.val+leftSum, node.val+rightSum, node.val+leftSum+rightSum)

            return max(node.val, node.val+leftSum, node.val+rightSum)
        
        dfs(root)
        return maxi