class MedianFinder:

    def __init__(self):
        # we need 2 heaps- smaller and larger
        self.lo=[] #max value at top so we negate
        self.hi=[] #min value at top
    def addNum(self, num: int) -> None:
        # when adding to the heaps 
        # we will have to rebalance
        # after rebalance lo will hold the extra element in case of odd nums
        heapq.heappush(self.lo, -num)
        # balace1- if lo's max > hi min
        if self.lo and self.hi and (-self.lo[0]> self.hi[0]):
            val= -heapq.heappop(self.lo)
            heapq.heappush(self.hi, val)
        # next we have to balance the lens of heap
        if len(self.lo) > len(self.hi)+1:
            val= -heapq.heappop(self.lo)
            heapq.heappush(self.hi, val)
        if len(self.hi) > len(self.lo):
            val= heapq.heappop(self.hi)
            heapq.heappush(self.lo, -val)

    def findMedian(self) -> float:
        # now medfian will either be self.lo[0] or mean of tops
        if len(self.lo)> len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0]+self.hi[0])/2.0
        
        