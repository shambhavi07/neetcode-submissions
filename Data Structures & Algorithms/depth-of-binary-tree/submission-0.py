# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # QUEUE + BFS APPROACH
        if not root:
            return 0
        queue= deque([root])
        depth=0
        while queue:
            # inside the queue we want to traverse level by level
            levelLen= len(queue)
            for _ in range(levelLen):
                node= queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth +=1
        
        return depth



        # e xplicit stack DFS
        # if not root:
        #     return 0
        # stack= [(root, 1)]
        # max_depth=0
        # while stack:
        #     node, depth= stack.pop()
        #     max_depth= max(max_depth, depth)
        #     if node.left:
        #         stack.append((node.left, depth+1))
        #     if node.right:
        #         stack.append((node.right, depth+1))
        # return max_depth



        # RECURSSIVE DFS
        # if not root:
        #     return 0
        
        # goleft = self.maxDepth(root.left)
        # goRight = self.maxDepth(root.right)

        # return 1 + max(goleft, goRight)