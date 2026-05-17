# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # early stop Time O(H+k)- — H to get to the leftmost node, then k steps
        # space O(H)- only recursion stack, no array
        self.count=0
        self.result=None

        def inorder(node):
            if not node or self.result is not None:
                return
            inorder(node.left)
            self.count +=1
            if self.count== k:
                self.result=node.val
                return
            inorder(node.right)
        inorder(root)
        return self.result






        #   Naive approach: Time O(n) soace O(n)+ recurssion stack o(h)
        # res=[]
        # def inorder(node):
        #     if not node: 
        #         return 
        #     inorder(node.left)
        #     res.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # return res[k-1]
        