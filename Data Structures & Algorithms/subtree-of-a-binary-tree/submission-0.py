# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        # q = deque()
        # if root:
        #     q.append(root)

        # level = 0
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

class Solution:   
    def findDepth(self, root:Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level
    
    def areEqual(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root2 and not root1:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.areEqual(root1.left, root2.left) and self.areEqual(root1.right, root2.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sublevel = self.findDepth(subRoot)
        level = self.findDepth(root)
        print(level, sublevel)
        if sublevel>level:
            return False
        q = deque()
        q.append(root)
        l = 0
        while level-l>sublevel:
            for i in range(len(q)):
                node = q.popleft()
                # x = self.areEqual(node, subRoot)
                # if x:
                #     return True

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l+=1
        for i in range(len(q)):
            node = q.popleft()
            x = self.areEqual(node, subRoot)
            if x:
                return True
        return False
        