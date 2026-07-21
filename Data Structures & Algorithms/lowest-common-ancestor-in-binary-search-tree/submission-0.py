# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        dq = deque()
        dq.append(root)
        p_node = None
        q_node = None
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node.val == p.val:
                    p_node = node
                if node.val == q.val:
                    q_node = node
                if node.left:
                    node.left.parent = node
                    dq.append(node.left)
                if node.right:
                    node.right.parent = node
                    dq.append(node.right)
        p_route = []
        q_route = []
        while p_node:
            p_route.append(p_node)
            p_node = p_node.parent
        while q_node:
            q_route.append(q_node)
            q_node = q_node.parent

        p_route = p_route[::-1]
        q_route = q_route[::-1]

        print([i.val for i in p_route])
        print([i.val for i in q_route])
        i =0
        while i<len(p_route) and i<len(q_route) and p_route[i].val == q_route[i].val:
            i+=1
        return p_route[i-1]