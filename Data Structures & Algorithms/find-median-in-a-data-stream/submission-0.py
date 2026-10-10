import heapq

class MedianFinder:

    def __init__(self):
        # max_heap stores the lower half (stores negative values to trick Python)
        self.max_heap = []
        # min_heap stores the upper half (stores normal positive values)
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Step 1: Push to max_heap (lower half)
        heapq.heappush(self.max_heap, -num)
        
        # Step 2: Order balancing — move the largest of lower half to upper half
        val = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, val)
        
        # Step 3: Size balancing — max_heap is allowed to have at most 1 extra element
        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        # If odd number of elements, the median is right at the top of max_heap
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        
        # If even, it's the average of both tops
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
