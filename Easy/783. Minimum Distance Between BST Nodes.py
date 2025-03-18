# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min_dis = float('inf')
        self.prev = None

        def inorder(node):
            if not node:
                return 

            inorder(node.left)

            if self.prev is not None:
                self.min_dis = min(self.min_dis, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.min_dis
