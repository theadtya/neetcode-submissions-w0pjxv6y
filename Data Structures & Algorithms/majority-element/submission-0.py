class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count= Counter(nums)
        res=0
        n= len(nums)
        for num in count:
            if count[num] > n//2:
                return num