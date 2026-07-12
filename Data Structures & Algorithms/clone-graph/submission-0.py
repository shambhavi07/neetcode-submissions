"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new= {}
        def dfs(n):
            # base case: check if already cloned
            if n in old_to_new:
                return old_to_new.get(n)
            # create clone of the node which should be an object of node
            clone= Node(n.val)
            old_to_new[n]= clone
            for neighbor in n.neighbors:
                nei= dfs(neighbor)
                clone.neighbors.append(nei)
            return clone




        return dfs(node)

        