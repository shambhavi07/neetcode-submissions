# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # result list that we will return
        result=[]
        if not root:
            return []

        queue= deque([root])
        while queue:
            level_size= len(queue)
            # sublist for each level 
            level=[]
            for _ in range(level_size):
                # pop the node
                node= queue.popleft()
                # append the popped node to level sublist
                level.append(node.val)
                # now add the children if any for the popped node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        # finally we have to add each level sunlist to final result list
            result.append(level)

        return result
        
        

        