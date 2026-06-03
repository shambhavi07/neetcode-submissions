class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create the max heap in pyhtin we will have to negate
        # create the list
        heap=[]
        for s in stones:
            heap.append(-s)
        # convert the list to heap
        heapq.heapify(heap)

        # we smash 2 largest weights until the len of heap is <= 1
        while len(heap) >1:
            # y when we pop we will have to negate back to get actual value
            y= -heapq.heappop(heap)
            # x
            x= -heapq.heappop(heap)
            # now if y is not equal to x remaider goes back to the array
            if y !=x:
                heapq.heappush(heap, -(y-x))
        if len(heap)==0:
            return 0
        return -heap[0]

        