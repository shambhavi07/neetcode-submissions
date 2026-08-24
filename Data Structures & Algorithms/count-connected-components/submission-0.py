class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap= {i:[] for i in range(n)}
        for u,v in edges:
            preMap[u].append(v)
            preMap[v].append(u)
        visited= set()

        components= 0
        def dfs(node):
            for nei in preMap[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        for node in range(n):
            if node not in visited:
                visited.add(node)
                components+=1
                dfs(node)
        return components