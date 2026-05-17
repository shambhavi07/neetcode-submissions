# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case
        if not preorder:
            return None
        
        # create root
        root= TreeNode(preorder[0])

        # find the split
        # we want to find the index/position of root value inside inorder
        # mid = inorder.index(preorder[0])
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        mid= inorder_idx[preorder[0]]

        # now we recurse
        root.left= self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right= self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

        