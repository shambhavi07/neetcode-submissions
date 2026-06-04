class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for x, y in points:
            dist= x**2 +y**2
            heapq.heappush(heap, (-dist, x,y))
            # pop from heap if len exceeds
            if len(heap) > k:
                heapq.heappop(heap)
        # extract just x,y from heap 
        res=[]
        for i in heap:
            x= i[1]
            y= i[2]
            res.append([x,y])
        return res
            
        
        