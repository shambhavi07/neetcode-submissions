class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap= {i: [] for i in range(numCourses)}
        indegree=[0]*numCourses
        for crs , pre in prerequisites:
            preMap[pre].append(crs)
            indegree[crs]+=1
        
        q= deque()
        for crs in range(numCourses):
            if indegree[crs]==0:
                q.append(crs)
        order=[]
        while q:
            node= q.popleft()
            order.append(node)
            for nei in preMap[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(order)== numCourses:
            return order
        else:
            return []
        

        

        