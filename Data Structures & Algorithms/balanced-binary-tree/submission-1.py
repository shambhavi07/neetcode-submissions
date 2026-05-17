class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # one pass solution o(n)- return [balancxhed, height]
        def dfs(node):
            if not node:
                return 0 #height for sa null is 0
            left_h= dfs(node.left)
            if left_h== -1:
                return -1
            right_h= dfs(node.right)
            if right_h ==-1:
                return -1
            if abs(left_h-right_h)>1:
                return -1
            return 1+ max(left_h,right_h)
        return dfs(root) !=-1






        # Naive approacgh: compute height for each node
        #  Time O(n^2):  For every node, you recompute heights by traversing entire subtrees. Node at the top recomputes heights of all nodes below it.
        # def height(node):
        #     if not node:
        #         return 0
        #     return 1+max(height(node.left), height(node.right))

        # if not root:
        #     return True
        # left_h= height(root.left)
        # right_h= height(root.right)
        # if abs(left_h -right_h) >1:
        #     return False
        # return self.isBalanced(root.left) and self.isBalanced(root.right)