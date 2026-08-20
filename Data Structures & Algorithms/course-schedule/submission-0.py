class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the map of each course to preq list
        preMap= {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # record all courses you visit on the current dfs path
        visitSet= set()
        def dfs(crs):
            # base case1: return False if we touch same node twice in the same dfs run
            if crs in visitSet:
                return False
            
            # base case 2: prereqs of this course is empty list i.e it has ni pre reqs
            if preMap[crs]==[]:
                return True

            # if none of the base case above
            # then we start processing the node by adding to path 
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True