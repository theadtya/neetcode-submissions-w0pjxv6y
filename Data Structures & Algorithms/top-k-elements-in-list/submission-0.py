class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter= Counter(nums)
        sorted_items= sorted(counter.items(),key= lambda x: x[1], reverse= True)
        return [num for num, count in sorted_items[:k]]
