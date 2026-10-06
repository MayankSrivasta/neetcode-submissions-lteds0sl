import heapq

class Solution:
    # Added 'self' as the first parameter
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        
        for x, y in points:
            # Invert distance to turn min-heap into a max-heap
            dist = -(x**2 + y**2)
            
            heapq.heappush(max_heap, (dist, [x, y]))
            
            # Keep the heap capped at size K
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        return [point for dist, point in max_heap]
