class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            return 1+max(height(node.left), height(node.right))

        if not root:
            return True
        left_h= height(root.left)
        right_h= height(root.right)
        if abs(left_h -right_h) >1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)