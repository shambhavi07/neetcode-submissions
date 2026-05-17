# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # iterative
        if not root: return 0

        stack = [root]
        height={} #node -> computed height
        diameter = 0
        while stack:
            node= stack[-1]
            if node.left and node.left not in height:
                stack.append(node.left)
            elif node.right and node.right not in height:
                stack.append(node.right)
            # both children do not exist or are done
            else:
                stack.pop()
                left_h = height.get(node.left, 0)
                right_h = height.get(node.right, 0)
                diameter = max(diameter, left_h+right_h)
                height[node]= 1+max(left_h,right_h)
        return diameter

        # self.diameter= 0 
        # def height(node):
        #     if not node:
        #         return 0
        #     left= height(node.left)
        #     right= height(node.right)
        #     self.diameter = max(self.diameter, left+right)
        #     return 1+ max(left, right)
        # height(root)
        # return self.diameter