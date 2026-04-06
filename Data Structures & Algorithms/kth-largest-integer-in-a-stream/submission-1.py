class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.minheap=nums
        # this needs becaause what happens if we have huge numbers at start, we need to throw rest
        # while len(self.minheap) >self.k:
        #     heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        heapq.heapify(self.minheap)
        while len(self.minheap) >self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
