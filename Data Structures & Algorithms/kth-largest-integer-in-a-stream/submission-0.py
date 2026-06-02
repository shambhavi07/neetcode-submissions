class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # turn input nums to a min heap
        self.k=k
        self.heap= nums
        heapq.heapify(self.heap)
        # now we only keep values in the heap so kth largest becomes o(1)op
        while len(self.heap) >k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # push val onto the heap
        heapq.heappush(self.heap, val)
        # check if len ofheap exceeds k values then pop min
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # finally return min
        return self.heap[0]

        
