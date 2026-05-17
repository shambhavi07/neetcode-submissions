# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursion
        if not root:
            return None
        # go down until leaft left
        left_inverted= self.invertTree(root.left)
        right_inverted=self.invertTree(root.right)

        root.left= right_inverted
        root.right= left_inverted
        return root



        # if not root:
        #     return None

        # # iterative stack- you control the stack using a list lifo. push root, process the children by swapping push their children onto stack and continue until stack is empty
        # stack = [root]
        # while stack:
        #     node= stack.pop()
        #     node.left, node.right= node.right, node.left
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return root
        