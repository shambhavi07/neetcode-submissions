class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # If node is None → append "N", return
        # Append node.val
        # Recurse left (which internally handles its own appending)
        # Recurse right (same)
        # At the top level, join and return
        result=[]
        def dfs(node):
            if not node:
                result.append("null")
                return
            # pre-order so append selfnfirst
            # convert to str as we want string
            result.append(str (node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)
             
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens= deque(data.split(","))
        def dfs():
            val= tokens.popleft()
            if val == "null":
                return None
            node= TreeNode(int(val))
            node.left= dfs()
            node.right=dfs()
            return node
        return dfs()