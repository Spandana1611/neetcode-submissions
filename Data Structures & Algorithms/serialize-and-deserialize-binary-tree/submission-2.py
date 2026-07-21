# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        left = ''
        if root.left:
            left = '(' + self.serialize(root.left) + ')'
        right = ''
        if root.right:
            right = '(' + self.serialize(root.right) + ')'
        ans = left+str(root.val)+ right
        # print(ans, root.val)
        return ans
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # print(data)
        if len(data) == 0:
            return None
        i = 0
        if data[0] == '(':
            i = 1
            bracs = 1
            while bracs != 0:
                if data[i] == '(':
                    bracs+=1 
                elif data[i] == ')':
                    bracs-=1
                i+=1
        val = 0
        j=i
        while j<len(data) and data[j] != '(' and data[j] != ')':
            val = 10*val + int(data[j])
            j+=1

        node = TreeNode(val)
        if i>0:
            node.left = self.deserialize(data[1:i-1])
        if j+1<len(data):
            node.right = self.deserialize(data[j+1:len(data)-1])
        return node
