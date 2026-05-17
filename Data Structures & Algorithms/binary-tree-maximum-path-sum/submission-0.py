# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=root.val

        def dfs(node):
            if not node:
                return 0
            nonlocal res

            leftGain= max(dfs(node.left),0)
            rightGain= max(dfs(node.right), 0)

            res= max(res, node.val+leftGain + rightGain)
            return node.val + max(leftGain, rightGain)
        dfs(root)
        return res
        