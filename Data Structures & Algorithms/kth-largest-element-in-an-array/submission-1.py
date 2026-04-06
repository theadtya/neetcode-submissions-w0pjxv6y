class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        res=[]
        while k>1:
            res.append(heapq.heappop_max(nums))
            k-=1
        return nums[0]
