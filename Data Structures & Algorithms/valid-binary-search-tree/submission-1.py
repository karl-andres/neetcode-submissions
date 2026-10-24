# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_array = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            inorder_array.append(node.val)
            dfs(node.right)
        
            return

        dfs(root)

        for i in range(len(inorder_array)):
            if i + 1 < len(inorder_array) and inorder_array[i] >= inorder_array[i + 1]:
                return False
        
        return True